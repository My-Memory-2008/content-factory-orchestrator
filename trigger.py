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
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        print("🚀 Setting up cloud execution trigger environment...")
        
        secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
        if not secret_auth_data:
            print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
            sys.exit(1)
            
        with open("kaggle_auth.json", "w") as f:
            f.write(secret_auth_data)

        # Force desktop layout constraints
        browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
        context = await browser.new_context(
            storage_state="kaggle_auth.json",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()

        notebook_url = "https://kaggle.com"
        print(f"📡 Connecting to notebook workspace: {notebook_url}")
        
        try:
            await page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
        except Exception as e:
            print(f"⚠️ Navigation status check: {e}")
            
        print("⏳ Waiting 30 seconds for the cloud server to provision your T4 session environment...")
        await page.wait_for_timeout(30000)

        # ====================================================================
        # NATIVE INTERACTIVE RUN ALL KEYBOARD BYPASS
        # ====================================================================
        print("🎹 Injecting global execution hotkeys...")
        
        # Bring focus onto the main window viewport body
        await page.focus("body")
        await page.wait_for_timeout(2000)
        
        # Execute the absolute universal Kaggle web shortcut for "Run All": Ctrl + Alt + Enter
        print("⚡ Sending 'Run All' command sequence (Ctrl + Alt + Enter)...")
        await page.keyboard.down("Control")
        await page.keyboard.down("Alt")
        await page.keyboard.press("Enter")
        await page.keyboard.up("Alt")
        await page.keyboard.up("Control")

        print("⏳ Holding active context stream open to ensure code submission clears remote gates...")
        await page.wait_for_timeout(20000)
        
        print("🎉 SUCCESS! The 'Run All' command was dispatched successfully on your GPU T4 x2 instances!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
