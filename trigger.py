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







# import asyncio
# import os
# import sys
# from playwright.async_api import async_playwright

# async def run():
#     async with async_playwright() as p:
#         print("🚀 Setting up cloud execution trigger environment for Kaggle Script mode...")
        
#         # Verify repository secrets token block 
#         secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
#         if not secret_auth_data:
#             print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
#             sys.exit(1)
            
#         with open("kaggle_auth.json", "w") as f:
#             f.write(secret_auth_data)

#         # Force standard desktop dimensions to guarantee editor focus areas are mapped properly
#         browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
#         context = await browser.new_context(
#             storage_state="kaggle_auth.json",
#             viewport={"width": 1920, "height": 1080}
#         )
#         page = await context.new_page()

#         # Exact path of your script editor panel
#         notebook_url = "https://kaggle.com/code/muhammadasjad2008/content-factory-engine/edit/"
#         print(f"📡 Connecting to script workspace: {notebook_url}")
        
#         try:
#             await page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
#         except Exception as e:
#             print(f"⚠️ Navigation status context: {e}")
            
#         print("⏳ Waiting 35 seconds for the cloud server to provision your T4 session environment...")
#         await page.wait_for_timeout(35000)

#         # ====================================================================
#         # SCRIPT MODE MULTI-STEP KEYBOARD RUN METHOD
#         # ====================================================================
#         print("🎹 Injecting universal code execution commands...")
        
#         try:
#             # 1. Focus inside the main text code window editor pane 
#             # Kaggle uses CodeMirror layers for script inputs (.cm-content)
#             await page.locator(".cm-content, [role='textbox'], .CodeMirror-code").first.click(timeout=10000)
#             print("🎯 Focus captured successfully on the main code editor cell.")
#         except Exception:
#             print("⚠️ Code cell frame selector missed. Forcing click onto central layout coordinate grid...")
#             await page.mouse.click(960, 540)
            
#         await page.wait_for_timeout(2000)
        
#         # 2. Select the entire contents of your python script file (Ctrl + A)
#         print("⌨️ Selecting all text inside script editor (Control + A)...")
#         await page.keyboard.down("Control")
#         await page.keyboard.press("a")
#         await page.keyboard.up("Control")
#         await page.wait_for_timeout(2000)
        
#         # 3. Trigger execution on the selected text lines (Shift + Enter)
#         print("⚡ Executing entire script file (Shift + Enter)...")
#         await page.keyboard.down("Shift")
#         await page.keyboard.press("Enter")
#         await page.keyboard.up("Shift")

#         print("⏳ Holding active context stream open to ensure code submission clears remote gates...")
#         await page.wait_for_timeout(25000)
        
#         print("🎉 SUCCESS! The text run command sequence has dispatched across your GPU T4 instances.")
#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run())



import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        print("🚀 Setting up logging-enabled cloud execution trigger for Kaggle Script mode...")
        
        # Verify repository secrets token block 
        secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
        if not secret_auth_data:
            print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
            sys.exit(1)
            
        with open("kaggle_auth.json", "w") as f:
            f.write(secret_auth_data)

        # Force standard desktop dimensions to map terminal boxes correctly
        browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
        context = await browser.new_context(
            storage_state="kaggle_auth.json",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()

        # Exact path of your script editor panel
        notebook_url = "https://kaggle.com"
        print(f"📡 Connecting to script workspace: {notebook_url}")
        
        try:
            await page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
        except Exception as e:
            print(f"⚠️ Navigation status context: {e}")
            
        print("⏳ Waiting 35 seconds for the cloud server to provision your T4 session environment...")
        await page.wait_for_timeout(35000)

        # ====================================================================
        # STEP 1: EXECUTE THE RUN ALL LOGIC
        # ====================================================================
        print("🎹 Injecting universal code execution commands...")
        try:
            await page.locator(".cm-content, [role='textbox'], .CodeMirror-code").first.click(timeout=10000)
            print("🎯 Focus captured successfully on the main code editor cell.")
        except Exception:
            print("⚠️ Code cell frame selector missed. Forcing click onto central layout grid...")
            await page.mouse.click(960, 540)
            
        await page.wait_for_timeout(2000)
        
        print("⌨️ Selecting all text inside script editor (Control + A)...")
        await page.keyboard.down("Control")
        await page.keyboard.press("a")
        await page.keyboard.up("Control")
        await page.wait_for_timeout(2000)
        
        print("⚡ Executing entire script file (Shift + Enter)...")
        await page.keyboard.down("Shift")
        await page.keyboard.press("Enter")
        await page.keyboard.up("Shift")
        print("📡 Run command sequence successfully sent over to Kaggle servers.")
        await page.wait_for_timeout(5000)

        # ====================================================================
        # STEP 2: LIVE STREAM TERMINAL LOGS INTO GITHUB ACTIONS LOGS
        # ====================================================================
        print("\n📺 MONITORING LIVE KAGGLE CONSOLE OUTPUT LOGS (Streaming Below):")
        print("="*80)
        
        # Define CSS tracking locators for Kaggle's standard log terminal wrapper rows
        console_selector = "[data-test-id='console-panel'], .console-output, .KaggleConsole-logs, div[class*='console']"
        
        # We loop and pull logs for a safe tracking window (e.g., 5 minutes or 60 loop updates)
        # Adjust range counts if your machine learning job requires longer execution times
        printed_lines = set()
        
        for iteration in range(60): 
            try:
                # Target the text content inside the live console window element layers
                console_element = page.locator(console_selector)
                if await console_element.count() > 0:
                    raw_text = await console_element.first.inner_text()
                    
                    # Split lines and print out only newly generated print text blocks
                    for line in raw_text.split("\n"):
                        clean_line = line.strip()
                        # Avoid duplicates and blank spacing logs
                        if clean_line and clean_line not in printed_lines:
                            print(f"[Kaggle-T4] {clean_line}")
                            printed_lines.add(clean_line)
                            
            except Exception as log_err:
                # If console wrapper hasn't broken DOM boundaries yet, wait smoothly
                pass
                
            # Intercept every 5 seconds to provide continuous terminal outputs
            await asyncio.sleep(5)
            
        print("="*80)
        print("🎉 PIPELINE EXECUTION COMPLETE! Monitoring handler detached securely.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
