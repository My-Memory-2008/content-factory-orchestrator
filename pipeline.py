import os
import cv2
import sys
import json
import torch
import shutil
import asyncio
import subprocess
import numpy as np
from PIL import Image
from curl_cffi import requests
from playwright.async_api import async_playwright
from transformers import AutoProcessor, AutoModelForMultimodalLM, BitsAndBytesConfig

# --- RECONFIGURED CONFLICT-FREE PATHS ---
INPUT_FILE = "input_reels.txt"
REJECTED_FILE = "rejected.txt"
FINAL_VAULT = "reel_source_summa.txt"
NEW_STORAGE_DIR = "curated_vault"  # Renamed from downloads

# Initialize the new workspace directory
os.makedirs(NEW_STORAGE_DIR, exist_ok=True)

# ==========================================
# STEP 1: QUEUE MANAGER & METADATA PRE-CHECK
# ==========================================
def get_and_clear_next_link():
    if not os.path.exists(INPUT_FILE):
        print(f"ℹ️ '{INPUT_FILE}' missing. Please create it and add your links.")
        sys.exit(0)

    with open(INPUT_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("📭 No new URLs found in your input file queue.")
        sys.exit(0)

    current_url = urls
    print(f"🎬 Selected Target Reel: {current_url}")

    # Instantly overwrite input_reels.txt excluding the target link
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
            likes = resp.json().get('items', [{}]).get('like_count', 0)
            print(f"📊 Engagement Metadata Found -> Likes: {likes}")
            if likes >= 50000:
                return current_url
            else:
                print(f"📉 Engagement too low (<50k). Logging to {REJECTED_FILE}")
                with open(REJECTED_FILE, "a") as f_rej:
                    f_rej.write(f"{current_url} - Low Engagement ({likes} likes)\n")
        else:
            print("⚠️ Metadata request restricted by Meta firewalls. Skipping.")
    except Exception as e:
        print(f"💥 Operational check failure: {e}")
    
    sys.exit(0)

# ==========================================
# STEP 2: PLAYWRIGHT STEALTH DOWNLOADER
# ==========================================
async def download_via_playwright(reel_url, output_file_path):
    print(f"🚀 Launching real browser instance to download from snapinsta.to: {reel_url}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        await page.route("**/*", lambda route: route.continue_() if not any(x in route.request.url for x in ["googlesyndication", "doubleclick", "adservice", "popads"]) else route.abort())
        
        await page.goto("https://snapinsta.to", wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(4000)
        
        input_selector = "input#s_input"
        await page.wait_for_selector(input_selector, timeout=15000)
        await page.fill(input_selector, reel_url)
        await page.wait_for_timeout(1000)
        
        submit_button_selector = "button:has-text('Download')"
        await page.click(submit_button_selector)
        
        try:
            close_selectors = [".modal-footer button", ".close", "button:has-text('Close')", "#close-button"]
            for sel in close_selectors:
                if await page.locator(sel).is_visible():
                    await page.click(sel)
        except Exception:
            pass
        
        download_btn_selector = "a:has-text('Download Video'), a[href*='cdninstagram.com'], a.btn-download"
        video_stream_url = None
        
        try:
            await page.wait_for_selector(download_btn_selector, timeout=25000)
            video_stream_url = await page.locator(download_btn_selector).first.get_attribute("href")
        except Exception as e:
            links = await page.locator("a").all()
            for link in links:
                href = await link.get_attribute("href")
                if href and ("instagram" in href or "cdn" in href or ".mp4" in href):
                    video_stream_url = href
                    break
                    
        await browser.close()
    
    if video_stream_url:
        video_stream_url = video_stream_url.replace('&amp;', '&')
        curl_cmd = ["curl", "-L", "-A", "Mozilla/5.0", "-o", output_file_path, video_stream_url]
        subprocess.run(curl_cmd, capture_output=True)
        if os.path.exists(output_file_path) and os.path.getsize(output_file_path) > 50000:
            print(f"🎉 Video download stream finalized successfully. Saved to: {output_file_path}")
            return True
    print("❌ Core video capture execution failed.")
    return False

# ==========================================
# STEP 3: FRAME MATRIX AND GEMMA AI INSPECTOR
# ==========================================
def run_gemma_ai_evaluation(reel_url, video_file_path):
    if not os.path.exists(video_file_path):
        return
        
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
        return

    prompt = (
        "Analyze these video frames thoroughly. You are acting as a strict quality control filter. "
        "Check all corners, edges, and the center for any kind of creator handle text, branding, application logo, "
        "or corporate promotional elements. Also, verify if a human face is clearly visible. "
        "If there are ANY watermarks, promotional logos, or human faces visible, reply with 'REJECT'. "
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
        print(f"❌ Rejected by AI. Logging tracking properties to {REJECTED_FILE}")
        with open(REJECTED_FILE, "a") as f_rej:
            f_rej.write(f"{reel_url} - Failed AI Custom Parameters\n")

    # Final workspace file cleanup
    if os.path.exists(video_file_path):
        os.remove(video_file_path)

# ==========================================
# MASTER ORCHESTRATION PIPELINE RUNNER
# ==========================================
if __name__ == "__main__":
    target_link = get_and_clear_next_link()
    
    # Extract unique shortcode from URL to dynamically define a unique filename
    try:
        shortcode = target_link.split("/reel/")[-1].split("/")[0]
    except Exception:
        shortcode = "unique_reel_asset"
        
    unique_video_name = f"reel_{shortcode}.mp4"
    dynamic_output_path = os.path.join(NEW_STORAGE_DIR, unique_video_name)
    
    download_success = asyncio.run(download_via_playwright(target_link, dynamic_output_path))
    if download_success:
        run_gemma_ai_evaluation(target_link, dynamic_output_path)
