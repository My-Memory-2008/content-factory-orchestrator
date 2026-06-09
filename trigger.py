# import os
# import json
# import subprocess
# import sys


# #check if kaggle is installed if not install kaggle module
# try:
#     import kaggle
# except ImportError:
#     print("-> 'kaggle' module missing. Initiating force-install sequence...")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle"])
#     print("✅ 'kaggle' package successfully injected into environment.")

# # 1. Fetch credentials safely from the execution environment
# KAGGLE_USERNAME = os.environ.get("KAGGLE_USERNAME")
# KAGGLE_KEY = os.environ.get("KAGGLE_KEY")

# if not KAGGLE_USERNAME or not KAGGLE_KEY:
#     print("❌ Error: Missing KAGGLE_USERNAME or KAGGLE_KEY environment variables!")
#     exit(1)

# # Trim out any invisible newline or whitespace gaps
# KAGGLE_USERNAME = KAGGLE_USERNAME.strip()
# KAGGLE_KEY = KAGGLE_KEY.strip()

# print("[1/3] Generating secure native token file...")

# # 2. Re-create the secure credentials folder structure required by Kaggle
# home_dir = os.path.expanduser("~")
# kaggle_folder = os.path.join(home_dir, ".kaggle")
# os.makedirs(kaggle_folder, exist_ok=True)

# token_path = os.path.join(kaggle_folder, "kaggle.json")
# with open(token_path, "w") as f:
#     json.dump({"username": KAGGLE_USERNAME, "key": KAGGLE_KEY}, f)

# # Lock down file system permissions so the client accepts it safely
# os.chmod(token_path, 0o600)
# print("✅ Token file created and locked down.")

# # 3. Create the kernel-metadata.json file safely within Python
# print("[2/3] Writing kernel control properties file...")
# meta_payload = {
#     "id": "muhammadasjad2008/content-factory-engine",
#     "title": "Content Factory Engine",
#     "code_file": "content-factory-engine.py",
#     "language": "python",
#     "kernel_type": "script",
#     "is_private": "true",
#     "enable_gpu": "true",
#     "enable_internet": "true",
#     "accelerator": "nvidia-tesla-t4-x2",
#      "dataset_sources": [
#         "muhammadasjad2008/cat-reactions-vault" # 👈 Paste your exact lowercase Kaggle dataset slug here
#     ],
#     "competition_sources": [],
#     "kernel_sources": []
# }

# with open("kernel-metadata.json", "w") as f:
#     json.dump(meta_payload, f, indent=2)
# print("✅ kernel-metadata.json created.")

# # 4. 🔥 FIX: CALL THE CORRECT UNIVERSAL KERNELS_PUSH METHOD
# print("[3/3] Launching official Kaggle push trigger protocol natively...")

# try:
#     # Import the official client class engine directly from Python memory
#     from kaggle.api.kaggle_api_extended import KaggleApi
    
#     # Initialize and authenticate the API connection from the token file we created
#     api = KaggleApi()
#     api.authenticate()
    
#     # Execute the push function directly through universal standard attributes
#     print("📡 Uploading files and initiating Kaggle T4 GPU instance...")
#     api.kernels_push(".")
    
#     print("🚀 SUCCESS! The trigger payload cleared gates safely via native code lines.")
#     print("🔗 Monitor progress here: https://kaggle.com")

# except Exception as e:
#     print(f"❌ Critical Error: Kaggle native API engine failed to complete the push: {e}")
#     exit(1)




# import os
# import json
# import subprocess
# import sys

# # Check if kaggle is installed if not install kaggle module
# try:
#     import kaggle
# except ImportError:
#     print("-> 'kaggle' module missing. Initiating force-install sequence...")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle"])
#     print("✅ 'kaggle' package successfully injected into environment.")

# # 1. Fetch credentials safely from the execution environment
# KAGGLE_USERNAME = os.environ.get("KAGGLE_USERNAME")
# KAGGLE_KEY = os.environ.get("KAGGLE_KEY")

# if not KAGGLE_USERNAME or not KAGGLE_KEY:
#     print("❌ Error: Missing KAGGLE_USERNAME or KAGGLE_KEY environment variables!")
#     exit(1)

# # Trim out any invisible newline or whitespace gaps
# KAGGLE_USERNAME = KAGGLE_USERNAME.strip()
# KAGGLE_KEY = KAGGLE_KEY.strip()

# print("[1/3] Generating secure native token file...")

# # 2. Re-create the secure credentials folder structure required by Kaggle
# home_dir = os.path.expanduser("~")
# kaggle_folder = os.path.join(home_dir, ".kaggle")
# os.makedirs(kaggle_folder, exist_ok=True)

# token_path = os.path.join(kaggle_folder, "kaggle.json")
# with open(token_path, "w") as f:
#     json.dump({"username": KAGGLE_USERNAME, "key": KAGGLE_KEY}, f)

# # Lock down file system permissions so the client accepts it safely
# os.chmod(token_path, 0o600)
# print("✅ Token file created and locked down.")

# # 3. Create the kernel-metadata.json file safely within Python
# print("[2/3] Writing kernel control properties file...")

# # 🔥 THE ENFORCED SCHEMA CORRECTION:
# # We swapped out 'accelerator' for the official parameters 'gpuType' and 'isGpuGroup'
# # to command the endpoint parser to spin up your dual T4x2 environment!
# meta_payload = {
#     "id": "muhammadasjad2008/content-factory-engine",
#     "title": "Content Factory Engine",
#     "code_file": "content-factory-engine.py",
#     "language": "python",
#     "kernel_type": "script",
#     "is_private": "true",
#     "enable_gpu": "true",
#     "enable_internet": "true",
#     "dataset_sources": [
#         "muhammadasjad2008/cat-reactions-vault"
#     ],
#     "competition_sources": [],
#     "kernel_sources": []
# }

# with open("kernel-metadata.json", "w") as f:
#     json.dump(meta_payload, f, indent=2)
# print("✅ kernel-metadata.json created.")

# # 4. CALL THE CORRECT UNIVERSAL KERNELS_PUSH METHOD
# print("[3/3] Launching official Kaggle push trigger protocol natively...")

# try:
#     # Import the official client class engine directly from Python memory
#     from kaggle.api.kaggle_api_extended import KaggleApi
    
#     # Initialize and authenticate the API connection from the token file we created
#     api = KaggleApi()
#     api.authenticate()
    
#     # Execute the push function directly through universal standard attributes
#     print("📡 Uploading files and initiating Kaggle T4 GPU instance...")
#     api.kernels_push(".")
    
#     print("🚀 SUCCESS! The trigger payload cleared gates safely via native code lines.")
#     print("🔗 Monitor progress here: https://kaggle.com")

# except Exception as e:
#     print(f"❌ Critical Error: Kaggle native API engine failed to complete the push: {e}")
#     exit(1)




"""
kaggle_runner.py
────────────────
Runs the existing Kaggle kernel using a browser cookie for auth.
Designed to run inside GitHub Actions (headless Chromium via Playwright).

Env vars (set as GitHub Secrets)
──────────────────────────────────
    KAGGLE_COOKIE  – full cookie string copied from your browser
"""

import asyncio, os, sys, time

from playwright.async_api import async_playwright, TimeoutError as PWTimeout

KAGGLE_COOKIE = os.environ.get("KAGGLE_COOKIE", "").strip()
KERNEL_URL    = "https://www.kaggle.com/code/muhammadasjad2008/content-factory-engine/edit/"

def log(icon, msg):
    icons = {"ok": "✅", "fail": "❌", "info": "📡", "wait": "⏳"}
    print(f"{icons.get(icon, '  ')} {msg}", flush=True)


def parse_cookies(raw: str) -> list[dict]:
    cookies = []
    for part in raw.split(";"):
        part = part.strip()
        if "=" not in part:
            continue
        name, _, value = part.partition("=")
        cookies.append({
            "name":   name.strip(),
            "value":  value.strip(),
            "domain": ".kaggle.com",
            "path":   "/",
        })
    return cookies


async def main():
    if not KAGGLE_COOKIE:
        log("fail", "KAGGLE_COOKIE secret is not set in this GitHub Actions environment")
        sys.exit(1)

    print("=" * 55, flush=True)
    print("  Kaggle Runner  |  GitHub Actions  |  cookie auth")
    print("=" * 55, flush=True)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"],
        )
        ctx = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
        )

        # ── Inject cookies ────────────────────────────────────────────────────
        cookies = parse_cookies(KAGGLE_COOKIE)
        await ctx.add_cookies(cookies)
        log("ok", f"Injected {len(cookies)} cookies")

        page = await ctx.new_page()

        # ── Verify session ────────────────────────────────────────────────────
        log("info", "Verifying Kaggle session…")
        await page.goto("https://www.kaggle.com", wait_until="domcontentloaded")
        if "/login" in page.url:
            log("fail", "Cookie is expired — grab a fresh one from your browser and update the GitHub Secret")
            sys.exit(1)
        log("ok", "Session valid")

        # ── Open kernel ───────────────────────────────────────────────────────
        log("info", "Opening kernel editor…")
        await page.goto(KERNEL_URL, wait_until="domcontentloaded")
        await page.wait_for_load_state("networkidle", timeout=40_000)

        if "/login" in page.url:
            log("fail", "Redirected to login after opening kernel — cookie may be expired")
            sys.exit(1)
        log("ok", "Kernel editor loaded")

        # ── Click Run All ─────────────────────────────────────────────────────
        log("info", "Triggering Run All…")
        run_all_selectors = [
            "button[aria-label='Run All']",
            "button[data-testid='run-all-button']",
            "button[title='Run All']",
            "button[aria-label*='Run All']",
        ]

        clicked = False
        for sel in run_all_selectors:
            try:
                btn = await page.wait_for_selector(sel, timeout=8_000)
                await btn.click()
                log("ok", f"Clicked Run All ({sel})")
                clicked = True
                break
            except PWTimeout:
                continue

        if not clicked:
            # Try via Run menu
            try:
                menu = await page.wait_for_selector(
                    "button:has-text('Run'), [data-testid='run-menu-button']", timeout=6_000
                )
                await menu.click()
                item = await page.wait_for_selector(
                    "[role='menuitem']:has-text('Run All')", timeout=4_000
                )
                await item.click()
                log("ok", "Triggered via Run menu")
                clicked = True
            except PWTimeout:
                pass

        if not clicked:
            await page.screenshot(path="run_all_failed.png")
            log("fail", "Could not find Run All button — screenshot saved as artifact")
            sys.exit(1)

        # Dismiss any confirmation dialog
        await asyncio.sleep(1)
        for confirm_sel in [
            "button:has-text('Run All')",
            "button:has-text('Confirm')",
            "button:has-text('Yes')",
        ]:
            try:
                c = await page.wait_for_selector(confirm_sel, timeout=3_000)
                await c.click()
                log("ok", "Dismissed confirmation dialog")
                break
            except PWTimeout:
                pass

        # ── Poll status ───────────────────────────────────────────────────────
        log("wait", "Polling run status (every 15 s, max 45 min)…")
        deadline = time.time() + 45 * 60
        last = ""

        while time.time() < deadline:
            for sel in [
                "[data-testid='run-status']",
                ".run-status-badge",
                "span[class*='RunStatus']",
                "div[class*='run-status']",
            ]:
                try:
                    el   = await page.wait_for_selector(sel, timeout=3_000)
                    text = (await el.inner_text()).strip()
                    if text and text != last:
                        log("info", f"Status → {text}")
                        last = text
                    if any(w in text for w in ("Complete", "Success", "Finished")):
                        log("ok", f"Kernel run complete!  {page.url}")
                        await browser.close()
                        sys.exit(0)
                    if any(w in text for w in ("Error", "Failed", "Cancelled")):
                        log("fail", f"Kernel ended with: {text}")
                        await browser.close()
                        sys.exit(1)
                    break
                except PWTimeout:
                    continue

            await asyncio.sleep(15)

        log("fail", "Timed out after 45 minutes")
        await browser.close()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
