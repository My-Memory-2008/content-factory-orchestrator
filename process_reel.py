# import os
# import cv2
# import json
# import re
# import base64
# import shutil
# import asyncio
# import requests
# import subprocess
# import time
# from playwright.async_api import async_playwright

# async def get_reel_likes_via_playwright(reel_url):
#     """
#     Launches Playwright to load the Instagram embed frame.
#     Uses multi-stage DOM parsing to reliably extract the exact like metric text.
#     """
#     print(f"🕵️  Checking like count via Playwright layout simulation: {reel_url}")
    
#     # Strip any query parameters and extract the shortcode
#     try:
#         clean_url = reel_url.split('?')[0]
#         if "/reel/" in clean_url:
#             shortcode = clean_url.split("/reel/")[-1].replace('/', '')
#         elif "/p/" in clean_url:
#             shortcode = clean_url.split("/p/")[-1].replace('/', '')
#         else:
#             print("❌ Invalid URL structure format provided.")
#             return 0
#     except Exception as e:
#         print(f"❌ Failed to parse shortcode string from URL: {e}")
#         return 0

#     embed_url = f"https://instagram.com/{shortcode}/embed/captioned/"
#     like_count = 0
    
#     async with async_playwright() as p:
#         try:
#             browser = await p.chromium.launch(
#                 headless=False,
#                 args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
#             )
#             context = await browser.new_context(
#                 viewport={'width': 1280, 'height': 720},
#                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
#             )
#             page = await context.new_page()
            
#             # Navigate to the embed view page
#             await page.goto(embed_url, wait_until="networkidle", timeout=30000)
#             await page.wait_for_timeout(4000)
            
#             # --- STRATEGY 1: Look for the visible text metric in the DOM elements ---
#             # Instagram embed displays likes inside elements containing text like 'likes' or '1,234 likes'
#             try:
#                 like_element = page.locator("a.EmbedShortcodeLikes, .EmbedShortcodeLikes, a[href*='liked_by']").first
#                 if await like_element.is_visible():
#                     text_content = await like_element.text_content()
#                     print(f"🔍 Found visible like text: '{text_content}'")
#                     # Extract numbers from text (e.g., "12,450 likes" -> 12450)
#                     numbers = re.findall(r'\d+', text_content.replace(',', '').replace('.', ''))
#                     if numbers:
#                         like_count = int(numbers[0])
#             except Exception as dom_err:
#                 print(f"⚠️ DOM extraction strategy skipped: {dom_err}")

#             # --- STRATEGY 2: Fallback to Page Source Context Parsing if DOM element search yielded 0 ---
#             if like_count == 0:
#                 page_content = await page.content()
                
#                 # Broad look for counts inside native JS metadata structural properties
#                 match = re.search(r'"edge_liked_by"\s*:\s*\{\s*"count"\s*:\s*(\d+)\}', page_content)
#                 if match:
#                     like_count = int(match.group(1))
#                 else:
#                     # Look for variations like "count":45123 inside generic interaction objects
#                     match_alt = re.search(r'"like_count"\s*:\s*(\d+)', page_content)
#                     if match_alt:
#                         like_count = int(match_alt.group(1))
#                     else:
#                         # Look for raw text strings in html like "55,231 likes"
#                         match_text = re.search(r'([\d,.]+)\s+likes', page_content, re.IGNORECASE)
#                         if match_text:
#                             like_count = int(match_text.group(1).replace(',', '').replace('.', ''))

#             await browser.close()
#         except Exception as e:
#             print(f"⚠️ Playwright like checker extraction failed completely: {e}")
            
#     return like_count

# async def run_stealth_download(reel_url, unique_id):
#     """Launches Playwright via Xvfb to grab source video downloads from snapinsta.to."""
#     if os.path.exists('checking_videos'):
#         shutil.rmtree('checking_videos')
        
#     os.makedirs('checking_videos', exist_ok=True)
#     output_path = f"checking_videos/reel_{unique_id}.mp4"
#     print(f"🚀 Initializing browser simulator for Snapinsta processing: {reel_url}")
#     video_stream_url = None
    
#     async with async_playwright() as p:
#         try:
#             browser = await p.chromium.launch(
#                 headless=False,
#                 args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
#             )
#             context = await browser.new_context(
#                 viewport={'width': 1280, 'height': 720},
#                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
#             )
#             page = await context.new_page()
#             await page.route("**/*", lambda r: r.continue_() if not any(x in r.request.url for x in ["googlesyndication", "doubleclick", "adservice", "popads"]) else r.abort())
            
#             await page.goto("https://snapinsta.to", wait_until="domcontentloaded", timeout=60000)
#             await page.wait_for_timeout(3000)
            
#             input_selector = "input#s_input"
#             await page.wait_for_selector(input_selector, timeout=15000)
#             await page.fill(input_selector, reel_url)
#             await page.wait_for_timeout(1000)
            
#             await page.click("button:has-text('Download')")
#             await page.wait_for_timeout(4000)
            
#             try:
#                 close_selectors = [".modal-footer button", ".close", "button:has-text('Close')"]
#                 for sel in close_selectors:
#                     if await page.locator(sel).is_visible():
#                         await page.click(sel)
#             except Exception:
#                 pass
                
#             download_btn_selector = "a:has-text('Download Video'), a[href*='cdninstagram.com'], a.btn-download"
#             await page.wait_for_selector(download_btn_selector, timeout=25000)
#             video_stream_url = await page.locator(download_btn_selector).first.get_attribute("href")
            
#         except Exception as e:
#             print(f"⚠️ Falling back to deep link exploration block: {e}")
#             try:
#                 links = await page.locator("a").all()
#                 for link in links:
#                     href = await link.get_attribute("href")
#                     if href and ("instagram" in href or "cdn" in href or ".mp4" in href):
#                         video_stream_url = href
#                         break
#             except Exception:
#                 pass
#         finally:
#             if 'browser' in locals():
#                 await browser.close()
                
#     if video_stream_url:
#         video_stream_url = video_stream_url.replace('&amp;', '&')
#         curl_cmd = ["curl", "-L", "-A", "Mozilla/5.0", "-o", output_path, video_stream_url]
#         subprocess.run(curl_cmd, capture_output=True)
#         if os.path.exists(output_path) and os.path.getsize(output_path) > 50000:
#             print(f"🎉 Asset extracted cleanly: {output_path}")
#             return output_path
            
#     return None

# def analyze_frame_with_qwen(frame_bytes):
#     """Sends compressed JPEG bytes directly into the local Qwen2.5-VL container."""
#     url = "http://localhost:11434/api/generate"
#     base64_image = base64.b64encode(frame_bytes).decode('utf-8')
    
#     prompt_text = (
#         "Analyze this image frame carefully. "
#         "Does it contain any human faces, brand logos, promotional text watermarks, or social handles? "
#         "Reply with exactly 'YES' if any of these are present, or 'NO' if the frame is completely clear and faceless."
#     )
    
#     payload = {"model": "qwen2.5vl:3b", "prompt": prompt_text, "images": [base64_image], "stream": False}
#     try:
#         response = requests.post(url, json=payload, timeout=45)
#         return response.json().get("response", "").strip().upper()
#     except Exception as e:
#         print(f"⚠️ Vision engine connectivity error: {e}")
#         return "YES"

# def analyze_video_frames(video_path):
#     """Extracts frame snapshots every 15 indices for vision inspection."""
#     cap = cv2.VideoCapture(video_path)
#     interval = 15
#     frame_count = 0
#     passed_check = True

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame_count += 1
#         if frame_count % interval == 0:
#             _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
#             ai_verdict = analyze_frame_with_qwen(buffer.tobytes())
#             print(f"Frame {frame_count} Evaluation Result: {ai_verdict}")
#             if "YES" in ai_verdict:
#                 print("❌ AI Verification Rejected: Frame contains face, branding, or watermarks.")
#                 passed_check = False
#                 break
#     cap.release()
#     return passed_check

# def commit_changes(reel_link, video_path=None):
#     """Syncs queue metrics, history listings, and video collections back to your GitHub repo."""
#     try:
#         subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
#         subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
#         subprocess.run(["git", "add", "input_link.txt", "reel_source_summa.txt", "rejected.txt"], check=True)
#         if video_path and os.path.exists(video_path):
#             subprocess.run(["git", "add", video_path], check=True)
#         subprocess.run(["git", "commit", "-m", f"Automated Pipeline: Processed single reel {reel_link}"], check=True)
#         subprocess.run(["git", "push"], check=True)
#         print("✅ Git Synchronization completed cleanly.")
    

#     except Exception as e:
#         print(f"⚠️ Git synchronization error: {e}")

# async def main():
#     if not os.path.exists("input_link.txt"):
#         print("ℹ️ Input queue input_link.txt file does not exist yet. Execution paused.")
#         return

#     with open("input_link.txt", "r") as f:
#         links = [line.strip() for line in f if line.strip()]

#     if not links:
#         print("Queue is empty. No links found in input_link.txt.")
#         return

#     # FIX: Extracted exactly the first single link string element instead of the raw array object list
#     current_reel = links[0]
#     remaining_links = links[1:]

#     with open("input_link.txt", "w") as f:
#         f.write("\n".join(remaining_links) + ("\n" if remaining_links else ""))

#     print(f"🎯 Processing Active Target String Link: {current_reel}")
#     likes = await get_reel_likes_via_playwright(current_reel)
#     print(f"📊 Like Metric Identified: {likes}")

#     if likes < 35000:
#         print("❌ Condition Failed: Reel has less than 50k likes. Adding to rejected.txt.")
#         with open("rejected.txt", "a") as f:
#             f.write(f"{current_reel} (Reason: Under 50k likes - Count: {likes})\n")
#         commit_changes(current_reel)
#         return

#     unique_id = int(time.time())
#     downloaded_file_path = await run_stealth_download(current_reel, unique_id)
    
#     if downloaded_file_path and os.path.exists(downloaded_file_path):
#         if analyze_video_frames(downloaded_file_path):
#             print("🎉 Success! Video completely clean. Appending link to reel_source_summa.txt.")
#             with open("reel_source_summa.txt", "a") as f:
#                 f.write(f"{current_reel}\n")
#             commit_changes(current_reel, video_path=downloaded_file_path)
#             return
#         else:

#             print("❌ Media link target parsing error. Adding to rejected.txt.")
#             with open("rejected.txt", "a") as f:
#                 f.write(f"{current_reel} (Reason: Snapinsta Download Stream Error)\n")

#         # Final execution wrap up push to sync tracking modifications
#         commit_changes(current_reel)

# if __name__ == "__main__":
#     asyncio.run(main())



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

async def run_stealth_download(reel_url, unique_id):
    """
    Launches a simulated Chromium browser instance inside Xvfb to 
    safely extract and download video stream elements from snapinsta.to.
    """
    if os.path.exists('checking_videos'):
        shutil.rmtree('checking_videos')
        
    os.makedirs('checking_videos', exist_ok=True)
    output_path = f"checking_videos/reel_{unique_id}.mp4"
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
            
            # Optimization: Kill trackers and slow ad networks to preserve runtime speeds
            await page.route("**/*", lambda r: r.continue_() if not any(x in r.request.url for x in ["googlesyndication", "doubleclick", "adservice", "popads"]) else r.abort())
            
            await page.goto("https://snapinsta.to", wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(3000)
            
            input_selector = "input#s_input"
            await page.wait_for_selector(input_selector, timeout=15000)
            
            # Ensure the input value is cast explicitly as a string to prevent Playwright list errors
            await page.fill(input_selector, str(reel_url))
            await page.wait_for_timeout(1000)
            
            await page.click("button:has-text('Download')")
            print("⏳ Monitoring layout transformations and scanning page elements...")
            # Give the backend server plenty of processing time to parse and display the download buttons
            await page.wait_for_timeout(12000)
            
            try:
                close_selectors = [".modal-footer button", ".close", "button:has-text('Close')"]
                for sel in close_selectors:
                    if await page.locator(sel).is_visible():
                        await page.click(sel)
            except Exception:
                pass
                
            # RESILIENT FALLBACK LOOP: Scans every link element on the page for video targets
            links = await page.locator("a").all()
            for link in links:
                href = await link.get_attribute("href")
                if href:
                    href_clean = href.lower()
                    if "cdninstagram" in href_clean or "://instagram.com" in href_clean or ".mp4" in href_clean or "download" in href_clean:
                        video_stream_url = href
                        print("🎯 Isolated valid download target URL stream match!")
                        break
            
        except Exception as e:
            print(f"⚠️ Exception within main browser context loop: {e}")
        finally:
            if 'browser' in locals():
                await browser.close()
                
    # FIX: Correctly process and return output path inside the download execution flow
    if video_stream_url:
        video_stream_url = video_stream_url.replace('&amp;', '&')
        curl_cmd = ["curl", "-L", "-A", "Mozilla/5.0", "-o", output_path, video_stream_url]
        subprocess.run(curl_cmd, capture_output=True)
        if os.path.exists(output_path) and os.path.getsize(output_path) > 50000:
            print(f"🎉 Asset extracted cleanly: {output_path}")
            return output_path
    else:
        print("❌ Could not isolate any direct video link properties on Snapinsta page layout panels.")
            
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
    
    payload = {"model": "qwen2.5vl:3b", "prompt": prompt_text, "images": [base64_image], "stream": False}
    try:
        # Long timeout threshold limit to survive CPU crunching restrictions on free runners
        response = requests.post(url, json=payload, timeout=180)
        return response.json().get("response", "").strip().upper()
    except Exception as e:
        print(f"⚠️ Vision engine connectivity error: {e}")
        return "YES"

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
        # FIX: Updated formatting syntax to a valid standard non-reply bot email configuration layout
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
        subprocess.run(["git", "add", "input_link.txt", "reel_source_summa.txt", "rejected.txt"], check=True)
        if video_path and os.path.exists(video_path):
            subprocess.run(["git", "add", video_path], check=True)
        subprocess.run(["git", "commit", "-m", f"Automated Pipeline: Processed single reel {reel_link}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Git Synchronization completed cleanly.")
    except Exception as e:
        print(f"⚠️ Git synchronization error: {e}")

async def main():
    if not os.path.exists("input_link.txt"):
        print("ℹ️ Input queue input_link.txt file does not exist yet. Execution paused.")
        return

    with open("input_link.txt", "r") as f:
        links = [line.strip() for line in f if line.strip()]

    if not links:
        print("Queue is empty. No links found in input_link.txt.")
        return

    # Extract EXACTLY the first index string element [0] from the links array list 
    current_reel = links[0]
    remaining_links = links[1:]

    with open("input_link.txt", "w") as f:
        f.write("\n".join(remaining_links) + ("\n" if remaining_links else ""))

    print(f"🎯 Processing Active Target String Link: {current_reel}")
    unique_id = int(time.time())
    
    downloaded_file_path = await run_stealth_download(current_reel, unique_id)
    
    if downloaded_file_path and os.path.exists(downloaded_file_path):
        if analyze_video_frames(downloaded_file_path):
            print("🎉 Success! Video completely clean. Appending link to reel_source_summa.txt.")
            with open("reel_source_summa.txt", "a") as f:
                f.write(f"{current_reel}\n")
            commit_changes(current_reel, video_path=downloaded_file_path)
            return
        else:
            # FIX: Completed the missing file cleanup step tracking execution criteria bounds
            print("❌ Video failed AI faceless/watermark inspection. Adding to rejected.txt.")
            with open("rejected.txt", "a") as f:
                f.write(f"{current_reel} (Reason: Failed Qwen Vision Check)\n")
            
            commit_changes(current_reel, video_path=downloaded_file_path)
            return
            
    else:
        print("❌ Media link target parsing error. Adding to rejected.txt.")
        with open("rejected.txt", "a") as f:
            f.write(f"{current_reel} (Reason: Snapinsta Download Stream Error)\n")

    commit_changes(current_reel)

if __name__ == "__main__":
    asyncio.run(main())
