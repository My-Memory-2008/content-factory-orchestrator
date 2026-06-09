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




import asyncio, os, sys, time

try:
    from playwright.async_api import async_playwright, TimeoutError as PWTimeout
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
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
        if not part or "=" not in part:
            continue
        name, _, value = part.partition("=")
        name  = name.strip()
        value = value.strip()
        if not name or not value:
            continue
        if any(c in name + value for c in ["\n", "\r", "\x00"]):
            continue
        cookies.append({"name": name, "value": value, "domain": ".kaggle.com", "path": "/"})
    return cookies


async def main():
    if not KAGGLE_COOKIE:
        log("fail", "KAGGLE_COOKIE secret is not set")
        sys.exit(1)

    cookies = parse_cookies(KAGGLE_COOKIE)
    log("info", f"Parsed {len(cookies)} cookies")

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

        injected = 0
        for cookie in cookies:
            try:
                await ctx.add_cookies([cookie])
                injected += 1
            except Exception as e:
                log("info", f"Skipped cookie '{cookie['name']}': {e}")
        log("ok", f"Injected {injected}/{len(cookies)} cookies")

        page = await ctx.new_page()

        # ── Verify session ────────────────────────────────────────────────────
        log("info", "Verifying Kaggle session…")
        await page.goto("https://www.kaggle.com", wait_until="domcontentloaded")
        if "/login" in page.url:
            log("fail", "Cookie expired — grab a fresh one and update the GitHub Secret")
            await page.screenshot(path="debug_login.png")
            sys.exit(1)
        log("ok", "Session valid")

        # ── Open kernel ───────────────────────────────────────────────────────
        log("info", "Opening kernel editor…")
        await page.goto(KERNEL_URL, wait_until="domcontentloaded")
        # Wait generously for React to fully render
        await asyncio.sleep(8)
        await page.screenshot(path="debug_editor.png")
        log("ok", "Kernel editor loaded — screenshot saved as debug_editor.png")

        if "/login" in page.url:
            log("fail", "Redirected to login — cookie may be expired")
            sys.exit(1)

        # ── Dump ALL buttons on page so we can see what's there ──────────────
        log("info", "Scanning all buttons on page…")
        buttons = await page.evaluate("""
            () => Array.from(document.querySelectorAll('button')).map(b => ({
                text:      b.innerText.trim().substring(0, 60),
                ariaLabel: b.getAttribute('aria-label') || '',
                title:     b.getAttribute('title') || '',
                testId:    b.getAttribute('data-testid') || '',
                classes:   b.className.substring(0, 80),
            }))
        """)
        log("info", f"Found {len(buttons)} buttons:")
        for b in buttons:
            print(f"    text='{b['text']}' | aria='{b['ariaLabel']}' | title='{b['title']}' | testid='{b['testId']}'", flush=True)

        # ── Try to find Save Version button (shown in your screenshot) ────────
        log("info", "Looking for Save Version button…")
        save_version_clicked = False

        # From your screenshot the button says "Save Version" in top-right area
        for sel in [
            "button:has-text('Save Version')",
            "button:has-text('Save version')",
            "button[data-testid='save-version-button']",
            "button[aria-label='Save Version']",
            "button[aria-label*='Save']",
            "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'save version')]",
        ]:
            try:
                by_xpath = sel.startswith("//")
                btn = await page.wait_for_selector(
                    f"xpath={sel}" if by_xpath else sel, timeout=6_000
                )
                await btn.click()
                log("ok", f"Clicked Save Version ({sel})")
                save_version_clicked = True
                break
            except PWTimeout:
                continue

        if not save_version_clicked:
            log("fail", "Could not find Save Version button — check debug_editor.png artifact")
            await browser.close()
            sys.exit(1)

        # ── Wait for the Save dialog ──────────────────────────────────────────
        log("info", "Waiting for Save dialog…")
        await asyncio.sleep(3)
        await page.screenshot(path="debug_dialog.png")
        log("info", "Dialog screenshot saved as debug_dialog.png")

        # ── Click the Save button inside the dialog ───────────────────────────
        log("info", "Clicking Save in dialog…")
        saved = False

        for sel in [
            "button:has-text('Save')",
            "[role='dialog'] button:has-text('Save')",
            "button[type='submit']",
            "//button[normalize-space(.)='Save']",
            "//button[contains(@class,'primary') and contains(.,'Save')]",
        ]:
            try:
                by_xpath = sel.startswith("//")
                btn = await page.wait_for_selector(
                    f"xpath={sel}" if by_xpath else sel, timeout=8_000
                )
                text = (await btn.inner_text()).strip()
                if text.lower() in ("cancel", "close", "dismiss"):
                    continue
                await btn.click()
                log("ok", f"Clicked Save button (text='{text}')")
                saved = True
                break
            except PWTimeout:
                continue

        if not saved:
            await page.screenshot(path="debug_save_failed.png")
            log("fail", "Could not click Save — check debug_save_failed.png artifact")
            await browser.close()
            sys.exit(1)

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
