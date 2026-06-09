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

        # Inject cookies one by one, skip bad ones
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
            sys.exit(1)
        log("ok", "Session valid")

        # ── Open kernel ───────────────────────────────────────────────────────
        log("info", "Opening kernel editor…")
        await page.goto(KERNEL_URL, wait_until="domcontentloaded")
        await page.wait_for_load_state("networkidle", timeout=40_000)
        if "/login" in page.url:
            log("fail", "Redirected to login — cookie may be expired")
            sys.exit(1)
        log("ok", "Kernel editor loaded")

        # ── Step 1: Click the ▶▶ Run All button (top-left of editor) ─────────
        log("info", "Clicking Run All (▶▶) button…")
        run_all_clicked = False

        # From the screenshot: the button has text "Run All" next to ▶▶ icon
        # Kaggle renders it as a button in the toolbar
        for sel in [
            "button:has-text('Run All')",
            "//button[contains(., 'Run All')]",
            "button[aria-label='Run All']",
            "button[data-testid='run-all-button']",
            "button[title='Run All']",
        ]:
            try:
                by_xpath = sel.startswith("//")
                if by_xpath:
                    btn = await page.wait_for_selector(f"xpath={sel}", timeout=10_000)
                else:
                    btn = await page.wait_for_selector(sel, timeout=10_000)
                await btn.click()
                log("ok", f"Clicked Run All button ({sel})")
                run_all_clicked = True
                break
            except PWTimeout:
                continue

        if not run_all_clicked:
            await page.screenshot(path="before_runall.png")
            log("fail", "Could not find Run All button — screenshot saved")
            sys.exit(1)

        # ── Step 2: Wait for "Save version" dialog to appear ─────────────────
        log("info", "Waiting for Save version dialog…")
        try:
            # The dialog has the heading "Save version"
            await page.wait_for_selector(
                "text='Save version', h2:has-text('Save version'), [role='dialog']:has-text('Save version')",
                timeout=15_000,
            )
            log("ok", "Save version dialog opened")
        except PWTimeout:
            await page.screenshot(path="no_dialog.png")
            log("fail", "Save version dialog did not appear — screenshot saved")
            sys.exit(1)

        # ── Step 3: Make sure "Save & Run All (Commit)" is selected ──────────
        # It's already selected by default (shown in screenshot), but let's confirm
        log("info", "Ensuring 'Save & Run All (Commit)' is selected…")
        try:
            # It's a dropdown — check if it already shows the right option
            dropdown = await page.wait_for_selector(
                "select, [role='combobox'], [role='listbox']",
                timeout=5_000,
            )
            current = await dropdown.inner_text()
            if "Save & Run All" not in current and "Commit" not in current:
                # Try to select the right option
                try:
                    await dropdown.select_option(label="Save & Run All (Commit)")
                    log("ok", "Selected 'Save & Run All (Commit)'")
                except Exception:
                    # Click it open and pick the option
                    await dropdown.click()
                    await asyncio.sleep(0.5)
                    opt = await page.wait_for_selector(
                        "text='Save & Run All (Commit)'", timeout=4_000
                    )
                    await opt.click()
                    log("ok", "Picked 'Save & Run All (Commit)' from dropdown")
            else:
                log("ok", "Save & Run All (Commit) already selected")
        except PWTimeout:
            log("info", "Could not find version type dropdown — proceeding with default")

        # ── Step 4: Click the final "Save" button in the dialog ──────────────
        log("info", "Clicking Save button in dialog…")
        saved = False

        for sel in [
            # The black "Save" button at the bottom-right of the dialog
            "button:has-text('Save')",
            "[role='dialog'] button:has-text('Save')",
            "button[type='submit']:has-text('Save')",
            "//button[normalize-space(.)='Save']",
        ]:
            try:
                by_xpath = sel.startswith("//")
                if by_xpath:
                    btn = await page.wait_for_selector(f"xpath={sel}", timeout=8_000)
                else:
                    btn = await page.wait_for_selector(sel, timeout=8_000)
                # Make sure it's not the Cancel button
                text = await btn.inner_text()
                if "Cancel" in text:
                    continue
                await btn.click()
                log("ok", "Clicked Save — kernel queued for execution")
                saved = True
                break
            except PWTimeout:
                continue

        if not saved:
            await page.screenshot(path="save_failed.png")
            log("fail", "Could not click Save button — screenshot saved")
            sys.exit(1)

        # ── Step 5: Poll run status ───────────────────────────────────────────
        log("wait", "Polling run status (every 15 s, max 45 min)…")
        deadline = time.time() + 45 * 60
        last = ""

        while time.time() < deadline:
            for sel in [
                "[data-testid='run-status']",
                ".run-status-badge",
                "span[class*='RunStatus']",
                "div[class*='run-status']",
                "text='Running'",
                "text='Complete'",
                "text='Error'",
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
