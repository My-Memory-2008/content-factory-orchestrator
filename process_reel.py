import os
import cv2
import json
import re
import base64
import shutil
import asyncio
import requests
import subprocess
import time
from playwright.async_api import async_playwright

def get_reel_likes(reel_url):
    """Parses public Instagram embed views to calculate interaction likes without a browser."""
    try:
        # Isolates the unique shortcode string from the url path
        if "/reel/" in reel_url:
            shortcode = reel_url.split("/reel/")[1].split("/")[0]
        elif "/p/" in reel_url:
            shortcode = reel_url.split("/p/")[1].split("/")[0]
        else:
            return 0
            
        embed_url = f"https://instagram.com{shortcode}/embed/captioned/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(embed_url, headers=headers, timeout=12)
        
        match = re.search(r'"edge_liked_by":\s*\{\s*"count":\s*(\d+)\}', response.text)
        if match:
            return int(match.group(1))
            
        match_alt = re.search(r'(\d+)\s+likes', response.text, re.IGNORECASE)
        if match_alt:
            return int(match_alt.group(1).replace(',', ''))
            
        return 0
    except Exception as e:
        print(f"⚠️ Metadata extraction skipped: {e}")
        return 0

async def run_stealth_download(reel_url, unique_id):
    """Launches Playwright Chromium via Xvfb to safely grab download streams from snapinsta.to."""
    if os.path.exists('downloads'):
        shutil.rmtree('downloads')
        
    os.makedirs('downloads', exist_ok=True)
    output_path = f"downloads/reel_{unique_id}.mp4"
    
    print(f"🚀 Initializing browser simulator for Snapinsta processing: {reel_url}")
    video_stream_url = None
    
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(
                headless=False,
                args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
            )
            context = await browser.new_context(
                viewport={'width': 1280, 'height': 720},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
            page = await context.new_page()
            
            # Optimization: Kill trackers and slow ad requests to preserve pipeline processing speed
            await page.route("**/*", lambda r: r.continue_() if not any(x in r.request.url for x in ["googlesyndication", "doubleclick", "adservice", "popads"]) else r.abort())
            
            await page.goto("https://snapinsta.to", wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(3000)
            
            input_selector = "input#s_input"
            await page.wait_for_selector(input_selector, timeout=15000)
            await page.fill(input_selector, reel_url)
            await page.wait_for_timeout(1000)
            
            await page.click("button:has-text('Download')")
            print("⏳ Parsing video cards down stream...")
            await page.wait_for_timeout(4000)
            
            # Dismiss rogue modal layout overlays if visible
            try:
                close_selectors = [".modal-footer button", ".close", "button:has-text('Close')"]
                for sel in close_selectors:
                    if await page.locator(sel).is_visible():
                        await page.click(sel)
            except Exception:
                pass
                
            download_btn_selector = "a:has-text('Download Video'), a[href*='cdninstagram.com'], a.btn-download"
            await page.wait_for_selector(download_btn_selector, timeout=25000)
            video_stream_url = await page.locator(download_btn_selector).first.get_attribute("href")
            
        except Exception as e:
            print(f"⚠️ Falling back to deep link exploration block: {e}")
            try:
                links = await page.locator("a").all()
                for link in links:
                    href = await link.get_attribute("href")
                    if href and ("instagram" in href or "cdn" in href or ".mp4" in href):
                        video_stream_url = href
                        break
            except Exception:
                pass
        finally:
            if 'browser' in locals():
                await browser.close()
                
    if video_stream_url:
        video_stream_url = video_stream_url.replace('&amp;', '&')
        curl_cmd = ["curl", "-L", "-A", "Mozilla/5.0", "-o", output_path, video_stream_url]
        subprocess.run(curl_cmd, capture_output=True)
        
        if os.path.exists(output_path) and os.path.getsize(output_path) > 50000:
            print(f"🎉 Asset extracted cleanly: {output_path}")
            return output_path
            
    return None

def analyze_frame_with_qwen(frame_bytes):
    """Sends compressed JPEG bytes directly into the local Qwen2.5-VL container."""
    url = "http://localhost:11434/api/generate"
    base64_image = base64.b64encode(frame_bytes).decode('utf-8')
    
    prompt_text = (
        "Analyze this image frame carefully. "
        "Does it contain any human faces, brand logos, promotional text watermarks, or social handles? "
        "Reply with exactly 'YES' if any of these are present, or 'NO' if the frame is completely clear and faceless."
    )
    
    payload = {
        "model": "qwen2.5-vl:3b-instruct-q4_K_M",
        "prompt": prompt_text,
        "images": [base64_image],
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload, timeout=45)
        output = response.json().get("response", "").strip().upper()
        return output
    except Exception as e:
        print(f"⚠️ Vision engine connectivity error: {e}")
        return "YES" # Defend repository asset integrity by defaulting to unsafe on system failure

def analyze_video_frames(video_path):
    """Extracts frame snapshots every 15 indices for vision inspection."""
    cap = cv2.VideoCapture(video_path)
    interval = 15
    frame_count = 0
    passed_check = True

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        if frame_count % interval == 0:
            # Compress image resolution by 75% to prevent system memory usage spikes
            _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
            
            ai_verdict = analyze_frame_with_qwen(buffer.tobytes())
            print(f"Frame {frame_count} Evaluation Result: {ai_verdict}")
            
            if "YES" in ai_verdict:
                print("❌ AI Verification Rejected: Frame contains face, branding, or watermarks.")
                passed_check = False
                break
                
    cap.release()
    return passed_check

def commit_changes(reel_link, video_path=None):
    """Syncs queue metrics, history listings, and video collections back to your GitHub repo."""
    try:
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@://github.com"], check=True)
        
        subprocess.run(["git", "add", "links.txt", "reel_source.txt", "rejected.txt"], check=True)
        if video_path and os.path.exists(video_path):
            subprocess.run(["git", "add", video_path], check=True)
            
        subprocess.run(["git", "commit", "-m", f"Automated Pipeline: Evaluated {reel_link}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Git Synchronization completed cleanly.")
    except Exception as e:
        print(f"⚠️ Git synchronization error: {e}")

def main():
    if not os.path.exists("links.txt"):
        print("ℹ️ Input queue links.txt file does not exist yet. Execution paused.")
        return

    with open("links.txt", "r") as f:
        links = [line.strip() for line in f if line.strip()]

    if not links:
        print("Queue is empty. No links found in links.txt.")
        return

    # Dequeue the target element (Pops exactly one reel per runtime)
    current_reel = links[0]
    remaining_links = links[1:]

    # CRITICAL FIX: Erases the processed link from links.txt immediately
    with open("links.txt", "w") as f:
        f.write("\n".join(remaining_links) + ("\n" if remaining_links else ""))

    print(f"🎯 Processing Active Target Target: {current_reel}")
    likes = get_reel_likes(current_reel)
    print(f"📊 Like Metric Identified: {likes}")

    if likes < 50000:
        print("❌ Condition Failed: Reel has less than 50k likes. Adding to rejected.txt.")
        with open("rejected.txt", "a") as f:
            f.write(f"{current_reel} (Reason: Under 50k likes - Count: {likes})\n")
        commit_changes(current_reel)
        return

    # Generate an incrementing timestamp ID string so new videos never overwrite old ones
    unique_id = int(time.time())
    downloaded_file_path = asyncio.run(run_stealth_download(current_reel, unique_id))
    
    if downloaded_file_path and os.path.exists(downloaded_file_path):
        if analyze_video_frames(downloaded_file_path):
            print("🎉 Success! Video completely clean. Appending link to reel_source.txt.")
            with open("reel_source.txt", "a") as f:
                f.write(f"{current_reel}\n")
            commit_changes(current_reel, video_path=downloaded_file_path)
            return
        else:
            print("❌ Video failed AI faceless/watermark inspection. Adding to rejected.txt.")
            with open("rejected.txt", "a") as f:
                f.write(f"{current_reel} (Reason: Failed Qwen Vision Check)\n")
            if os.path.exists(downloaded_file_path):
                os.remove(downloaded_file_path)
    else:
        print("❌ Media link target parsing error. Adding to rejected.txt.")
        with open("rejected.txt", "a") as f:
            f.write(f"{current_reel} (Reason: Snapinsta Download Stream Error)\n")

    # Final execution wrap up push to sync tracking modifications
    commit_changes(current_reel)

if __name__ == "__main__":
    main()
