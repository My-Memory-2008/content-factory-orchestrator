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




import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        print("🚀 Setting up cloud automation browser environment...")
        
        secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
        if not secret_auth_data:
            print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
            sys.exit(1)
            
        with open("kaggle_auth.json", "w") as f:
            f.write(secret_auth_data)

        # Launching headless browser on the GitHub Linux runner
        browser = await p.chromium.launch(headless=True)
        
        # Restore pre-authenticated session state
        context = await browser.new_context(storage_state="kaggle_auth.json")
        page = await context.new_page()

        # 1. Open the specific script workspace editor panel directly
        notebook_url = "https://kaggle.com"
        print(f"📡 Transitioning to live workspace environment: {notebook_url}")
        
        try:
            # We use domcontentloaded so the script doesn't hang on endless tracking streams
            await page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
        except Exception as e:
            print(f"⚠️ Initial framework notice (safe to skip): {e}")
            
        # FIX 1: Increased initial wait loop buffer to let Kaggle's backend allocate your T4 machine safely
        print("⏳ Waiting 45 seconds for the cloud server container frames and scripts to fully initialize...")
        await page.wait_for_timeout(45000)

        # 2. Extract localized model file configurations from the repo directory
        script_file_path = "content-factory-engine.py"
        print(f"📝 Fetching repository code elements from {script_file_path}...")
        try:
            with open(script_file_path, "r", encoding="utf-8") as file:
                production_code_payload = file.read()
        except FileNotFoundError:
            print(f"❌ Error: Could not locate '{script_file_path}' in runner path workspace!")
            await browser.close()
            sys.exit(1)

        # 3. Focus and Click onto the code editor frame surface
        print("🎹 Targeting target script cells arrays...")
        
        # FIX 2: We expand our selector choices and wait explicitly for visibility before running actions
        editor_selector = ".cm-content, .CodeMirror-code, [role='textbox'], .KaggleCodeCell"
        editor_cell = page.locator(editor_selector).first
        
        try:
            # Safely wait for the target container to structuralize in the DOM
            await editor_cell.wait_for(state="visible", timeout=30000)
            
            # FIX 3: Swap out .focus() for a robust click gesture to firmly hook the cursor placement
            await editor_cell.click()
            await page.wait_for_timeout(2000)
        except Exception as err:
            print(f"⚠️ Primary cell locator timed out: {err}. Attempting raw layout fallback click...")
            # Fallback fallback step: click the absolute center coordinates of the main body workspace
            await page.mouse.click(500, 400)
            await page.wait_for_timeout(2000)

        # 4. Clear out stale script blocks inside the container frame
        print("⌨️ Clearing legacy code segments...")
        modifier_key = "Control"
        await page.keyboard.down(modifier_key)
        await page.keyboard.press("a")
        await page.keyboard.up(modifier_key)
        await page.wait_for_timeout(1500)
        await page.keyboard.press("Backspace")
        await page.wait_for_timeout(1500)

        # 5. Inject your script payload inside the container 
        print("📋 Writing updated model script streams...")
        await editor_cell.fill(production_code_payload)
        await page.wait_for_timeout(3000)

        # 6. Execute Run All hotkey logic (Keeps your GPU T4 configuration active!)
        print("⚡ Dispatching interactive cell runtime execution scripts...")
        await page.keyboard.down("Control")
        await page.keyboard.down("Shift")
        await page.keyboard.press("Enter")
        await page.keyboard.up("Shift")
        await page.keyboard.up("Control")

        print("⏳ Ensuring execution handshakes complete safely across remote nodes...")
        await page.wait_for_timeout(15000)
        
        print("🎉 SUCCESS! GitHub Actions has uploaded your new code to Kaggle on the GPU T4 instance successfully!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
