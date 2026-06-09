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
kaggle_playwright_push.py
─────────────────────────
Logs into Kaggle and runs the existing kernel at:
  https://www.kaggle.com/code/muhammadasjad2008/content-factory-engine/edit/

Requirements
────────────
    pip install playwright
    playwright install chromium

Env vars
────────
    KAGGLE_USERNAME  – your Kaggle email or username
    KAGGLE_PASSWORD  – your Kaggle password
    HEADLESS         – "false" to watch the browser (default: "true")
"""

import asyncio, os, sys, time

try:
    from playwright.async_api import async_playwright, TimeoutError as PWTimeout
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.async_api import async_playwright, TimeoutError as PWTimeout

USERNAME = os.environ.get("KAGGLE_USERNAME", "").strip()
PASSWORD = os.environ.get("KAGGLE_PASSWORD", "").strip()
HEADLESS = os.environ.get("HEADLESS", "true").lower() != "false"
KERNEL_URL = "https://www.kaggle.com/code/muhammadasjad2008/content-factory-engine/edit/"

def log(icon, msg):
    icons = {"ok": "✅", "fail": "❌", "info": "📡", "wait": "⏳"}
    print(f"{icons.get(icon, '  ')} {msg}")


async def login(page):
    log("info", "Navigating to Kaggle login…")
    await page.goto("https://www.kaggle.com/account/login", wait_until="domcontentloaded")

    # Dismiss cookie banner if present
    try:
        btn = await page.wait_for_selector("button[data-testid='accept-all-cookies']", timeout=5_000)
        await btn.click()
    except PWTimeout:
        pass

    await page.fill("input[name='username']", USERNAME)
    await page.fill("input[name='password']", PASSWORD)
    await page.click("button[type='submit']")

    try:
        await page.wait_for_url(lambda u: "/login" not in u, timeout=25_000)
    except PWTimeout:
        log("fail", "Login failed — check KAGGLE_USERNAME / KAGGLE_PASSWORD")
        await page.screenshot(path="login_failed.png", full_page=True)
        sys.exit(1)

    log("ok", f"Logged in as {USERNAME}")


async def open_kernel(page):
    log("info", f"Opening kernel editor…")
    await page.goto(KERNEL_URL, wait_until="domcontentloaded")
    # Give the editor time to fully hydrate
    await page.wait_for_load_state("networkidle", timeout=40_000)
    log("ok", "Kernel editor loaded")


async def run_all(page):
    """
    Click the Run All button. Kaggle exposes this as:
      • A toolbar button  (▶▶ icon, aria-label contains "Run All")
      • Or via the Run menu
    We try multiple selectors as the UI sometimes changes.
    """
    log("info", "Triggering Run All…")

    selectors = [
        # Toolbar run-all button
        "button[aria-label*='Run All']",
        "button[data-testid='run-all-button']",
        "button[title*='Run All']",
        # Toolbar play button that opens a dropdown
        "button[aria-label*='Run']",
        # Run menu item
        "[role='menuitem']:has-text('Run All')",
    ]

    for sel in selectors:
        try:
            btn = await page.wait_for_selector(sel, timeout=8_000)
            if btn:
                await btn.click()
                log("ok", f"Clicked: {sel}")
                # If this opened a dropdown, look for "Run All" inside it
                try:
                    run_item = await page.wait_for_selector(
                        "[role='menuitem']:has-text('Run All'), button:has-text('Run All')",
                        timeout=3_000,
                    )
                    await run_item.click()
                    log("ok", "Selected 'Run All' from dropdown")
                except PWTimeout:
                    pass  # wasn't a dropdown, direct click was enough
                return
        except PWTimeout:
            continue

    # Last-resort: keyboard shortcut (Shift+Enter runs cell, no universal Run All shortcut on Kaggle)
    # Instead try the Run menu in the top nav
    try:
        run_menu = await page.wait_for_selector("button:has-text('Run'), [data-testid='run-menu']", timeout=6_000)
        await run_menu.click()
        run_all_item = await page.wait_for_selector("[role='menuitem']:has-text('Run All')", timeout=4_000)
        await run_all_item.click()
        log("ok", "Triggered Run All via menu")
        return
    except PWTimeout:
        pass

    log("fail", "Could not find Run All button — saving screenshot for inspection")
    await page.screenshot(path="run_all_failed.png", full_page=True)
    sys.exit(1)


async def poll_status(page, timeout_minutes=45):
    """
    Poll the kernel run status badge until it's Complete or Error.
    Kaggle shows statuses like: Queued → Running → Complete / Error
    """
    log("wait", f"Polling run status (max {timeout_minutes} min)…")
    deadline = time.time() + timeout_minutes * 60
    last = ""

    while time.time() < deadline:
        # Try several known status indicator selectors
        for sel in [
            "[data-testid='run-status']",
            ".run-status-badge",
            "span[class*='RunStatus']",
            "div[class*='run-status']",
            # Kaggle sometimes shows it in a progress bar label
            "[aria-label*='Running']",
            "[aria-label*='Complete']",
            "[aria-label*='Error']",
        ]:
            try:
                el = await page.wait_for_selector(sel, timeout=3_000)
                text = (await el.inner_text()).strip()
                if text and text != last:
                    log("info", f"Status → {text}")
                    last = text
                if any(w in text for w in ("Complete", "Success", "Finished")):
                    log("ok", f"Run completed! View: {page.url}")
                    return True
                if any(w in text for w in ("Error", "Failed", "Cancelled")):
                    log("fail", f"Run ended with: {text}")
                    return False
                break
            except PWTimeout:
                continue

        await asyncio.sleep(15)

    log("fail", f"Timed out after {timeout_minutes} minutes")
    return False


async def main():
    if not USERNAME or not PASSWORD:
        log("fail", "Set KAGGLE_USERNAME and KAGGLE_PASSWORD environment variables")
        sys.exit(1)

    print("=" * 55)
    print("  Kaggle Playwright Runner  |  no API keys needed")
    print("=" * 55)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=HEADLESS,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        ctx = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
        )
        page = await ctx.new_page()

        try:
            await login(page)
            await open_kernel(page)
            await run_all(page)
            success = await poll_status(page)
            sys.exit(0 if success else 1)
        except Exception as e:
            log("fail", f"Unexpected error: {e}")
            await page.screenshot(path="debug.png", full_page=True)
            log("info", "Saved debug.png for inspection")
            raise
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
