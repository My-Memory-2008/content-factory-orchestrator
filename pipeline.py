import os
import cv2
import sys
import shutil
import torch
import numpy as np
from PIL import Image
from transformers import AutoProcessor, AutoModelForMultimodalLM, BitsAndBytesConfig

FINAL_VAULT = "reel_source.txt"
REJECTED_FILE = "rejected.txt"
NEW_STORAGE_DIR = "curated_vault"

def log_failure(url, reason):
    print(f"❌ PIPELINE REJECTION: {url} -> Reason: {reason}")
    with open(REJECTED_FILE, "a") as f_rej:
        f_rej.write(f"{url} - {reason}\n")

def run_gemma_ai_evaluation():
    # Detect the filename generated dynamically inside the workspace
    if not os.path.exists(NEW_STORAGE_DIR):
        print("ℹ️ Storage directory missing. Skipping AI cycle.")
        return

    files = [f for f in os.listdir(NEW_STORAGE_DIR) if f.endswith(".mp4")]
    if not files:
        print("ℹ️ No download target file found to process. Skipping AI verification.")
        return

    video_file_name = files[0]
    video_file_path = os.path.join(NEW_STORAGE_DIR, video_file_name)
    
    # Extract raw URL back from filename reconstruction (reel_shortcode.mp4)
    shortcode = video_file_name.replace("reel_", "").replace(".mp4", "")
    reel_url = f"https://instagram.com{shortcode}/"
        
    try:
        print("🧠 Loading Quantized Gemma Multimodal Model...")
        quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
        MODEL_ID = "google/gemma-4-E2B-it"
        model = AutoModelForMultimodalLM.from_pretrained(MODEL_ID, quantization_config=quantization_config, device_map="cpu")
        processor = AutoProcessor.from_pretrained(MODEL_ID)

        print("🎞️ Slicing video into 15-frame matrix increments...")
        cap = cv2.VideoCapture(video_file_path)
        frames = []
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % 15 == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frames.append(Image.fromarray(frame_rgb))
            frame_count += 1
        cap.release()

        if not frames:
            log_failure(reel_url, "OpenCV failed to parse video structural frames cleanly.")
            return

        prompt = (
            "Analyze these video frames thoroughly. You are acting as a strict quality control filter. "
        "Check all corners, edges, and the center for any kind of creator handle text, branding, application logo, "
        "or corporate promotional elements. Also, verify if a human face is clearly visible who promotes himself and the frame looks like faceless video. "
        "If there are ANY watermarks, promotional logos, or human faces visible who promote themselves through branding and for subscription or following, reply with 'REJECT'. "
        "If the video is completely faceless AND completely free of any branding/watermarks, reply with 'APPROVE'."
        )
        
        messages = [{"role": "user", "content": [{"type": "video", "video": frames}, {"type": "text", "text": prompt}]}]
        formatted_prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
        inputs = processor(text=formatted_prompt, images=frames, return_tensors="pt").to("cpu")
        
        with torch.no_grad():
            output_ids = model.generate(**inputs, max_new_tokens=10)
            
        response = processor.decode(output_ids, skip_special_tokens=True).strip().upper()
        print(f"📋 AI Evaluation Response: {response}")

        if "APPROVE" in response:
            print(f"🏆 Video Verified! Appending to {FINAL_VAULT}")
            with open(FINAL_VAULT, "a") as f_vault:
                f_vault.write(f"{reel_url}\n")
        else:
            log_failure(reel_url, "Failed AI Parameters (Watermark, Brand logo, or Face detected)")

    except Exception as e:
        log_failure(reel_url, f"Gemma Evaluation Stage Crash: {str(e)}")
    finally:
        # Guarantee local workspace is wiped clean
        if os.path.exists(NEW_STORAGE_DIR):
            shutil.rmtree(NEW_STORAGE_DIR)

if __name__ == "__main__":
    run_gemma_ai_evaluation()
