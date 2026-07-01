import os
import cv2
import sys
import torch
import numpy as np
from PIL import Image
from curl_cffi import requests
from transformers import AutoProcessor, AutoModelForMultimodalLM, BitsAndBytesConfig

INPUT_FILE = "input_reels.txt"
REJECTED_FILE = "rejected.txt"
FINAL_VAULT = "reel_source.txt"
TARGET_TRACKER = "current_target.txt"

def log_failure(url, reason):
    print(f"❌ PIPELINE REJECTION: {url} -> Reason: {reason}")
    with open(REJECTED_FILE, "a") as f_rej:
        f_rej.write(f"{url} - {reason}\n")

# ==========================================
# PHASE 1: QUEUE MANAGER & METADATA PRE-CHECK
# ==========================================
def run_pre_check():
    if not os.path.exists(INPUT_FILE):
        print(f"ℹ️ '{INPUT_FILE}' missing. Please create it and add your links.")
        sys.exit(0)

    with open(INPUT_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("📭 No new URLs found in your input file queue.")
        sys.exit(0)

    current_url = urls[0]
    print(f"🎬 Selected Target Reel: {current_url}")

    # Remove immediately from the input queue file
    with open(INPUT_FILE, "w") as f:
        for remaining_url in urls[1:]:
            f.write(f"{remaining_url}\n")
    print("🧹 Queue Updated: Target link permanently cleared from input_reels.txt.")
    
    # Check Instagram engagement statistics
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        meta_url = f"{current_url}/?__a=1&__d=dis"
        resp = requests.get(meta_url, headers=headers, impersonate="chrome120")
        
        if resp.status_code == 200:
            items = resp.json().get('items', [])
            likes = items[0].get('like_count', 0) if items else 0
            print(f"📊 Engagement Metadata Found -> Likes: {likes}")
            
            if likes >= 50000:
                # Save target URL to temporary tracker file for the YAML workflow to read
                with open(TARGET_TRACKER, "w") as f_target:
                    f_target.write(current_url)
                print(f"✅ Metric approved. Link written to {TARGET_TRACKER}")
                return
            else:
                log_failure(current_url, f"Low Engagement ({likes} likes)")
        else:
            log_failure(current_url, f"Instagram Firewall Blocked Metadata Request (Status Code: {resp.status_code})")
    except Exception as e:
        log_failure(current_url, f"Metadata Parsing Exception Error: {str(e)}")
    
    sys.exit(0)

# ==========================================
# PHASE 2: GEMMA AI FRAME INSPECTOR
# ==========================================
def run_gemma_ai_evaluation():
    if not os.path.exists(TARGET_TRACKER):
        print("ℹ️ Target tracker file missing. Skipping AI cycle.")
        return

    with open(TARGET_TRACKER, "r") as f:
        reel_url = f.read().strip()

    # Locate the video file downloaded by the YAML Playwright step
    video_file_path = None
    if os.path.exists("curated_vault"):
        files = [os.path.join("curated_vault", f) for f in os.listdir("curated_vault") if f.endswith(".mp4")]
        if files:
            video_file_path = files[0]

    if not video_file_path or not os.path.exists(video_file_path):
        log_failure(reel_url, "Missing downloaded video file during AI verification stage.")
        cleanup_temp_files()
        return
        
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
            cleanup_temp_files()
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
        cleanup_temp_files()

def cleanup_temp_files():
    if os.path.exists("curated_vault"):
        shutil.rmtree("curated_vault")
    if os.path.exists(TARGET_TRACKER):
        os.remove(TARGET_TRACKER)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--gemma":
        run_gemma_ai_evaluation()
    else:
        run_pre_check()
