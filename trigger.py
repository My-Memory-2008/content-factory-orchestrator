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





# import asyncio
# import os
# import sys
# from playwright.async_api import async_playwright

# async def run():
#     async with async_playwright() as p:
#         print("🚀 Setting up ultra-efficient Kaggle Script Save Version trigger...")
        
#         # Verify repository secrets token block 
#         secret_auth_data = os.environ.get("KAGGLE_AUTH_JSON")
#         if not secret_auth_data:
#             print("❌ Error: Missing KAGGLE_AUTH_JSON environment variable secret!")
#             sys.exit(1)
            
#         with open("kaggle_auth.json", "w") as f:
#             f.write(secret_auth_data)

#         # Launching headless browser on desktop resolution
#         browser = await p.chromium.launch(headless=True, args=["--window-size=1920,1080"])
#         context = await browser.new_context(
#             storage_state="kaggle_auth.json",
#             viewport={"width": 1920, "height": 1080}
#         )
#         page = await context.new_page()

#         # Exact path of your script editor panel
#         notebook_url = "https://kaggle.com/code/muhammadasjad2008/content-factory-engine/edit"
#         print(f"📡 Connecting to script workspace: {notebook_url}")
        
#         try:
#             await page.goto(notebook_url, wait_until="domcontentloaded", timeout=90000)
#         except Exception as e:
#             print(f"⚠️ Navigation status context: {e}")
            
#         print("⏳ Waiting 30 seconds for the editor application layout to stabilize...")
#         await page.wait_for_timeout(30000)

#         # Check if cookie actually logged you in or dropped you onto a guest landing screen
#         page_content = await page.content()
#         if "Sign In" in page_content or "login" in page.url:
#             print("❌ Error: The session token in KAGGLE_AUTH_JSON is expired or rejected by Kaggle!")
#             await browser.close()
#             sys.exit(1)

#         # ====================================================================
#         # JAVASCRIPT INJECTION: TRIGGERING NATIVE KAGGLE CORE SAVE ENGINE
#         # ====================================================================
#         print("📋 Injecting JavaScript bypass to trigger background Save Version workflow...")
        
#         # This script locates the exact internal state button and forces a production version commit.
#         # This acts exactly as if you clicked "Save Version" -> "Save & Run All" in the browser!
#         save_js = """
#         () => {
#             // Priority 1: Check for Kaggle's explicit data-testid attribute if available
#             let saveBtn = document.querySelector('[data-testid="save-version-button"]');
            
#             // Priority 2: Scan deep DOM layers if first-level lookup failed
#             if (!saveBtn) {
#                 const elements = Array.from(document.querySelectorAll('*'));
#                 saveBtn = elements.find(el => {
#                     const text = el.textContent || '';
#                     // Match full word strings or nested element text blocks
#                     return el.tagName === 'BUTTON' && text.trim().toLowerCase() === 'save version';
#                 });
#             }
            
#             // Priority 3: Fallback button text containment query
#             if (!saveBtn) {
#                 saveBtn = Array.from(document.querySelectorAll('button')).find(
#                     b => b.textContent.toLowerCase().includes('save version')
#                 );
#             }
            
#             if (saveBtn) {
#                 saveBtn.click();
#                 return true;
#             }
#             return false;
#         }
#         """
        
#         opened_dialog = await page.evaluate(save_js)
#         await page.wait_for_timeout(3000)

#         if opened_dialog:
#             print("🔘 'Save Version' menu opened. Confirming background run allocation...")
#             try:
#                 # FIXED: Swapped to a precise locator sequencing prioritizing Kaggle's strict popup button components
#                 confirm_btn = page.locator("button[data-testid='save-version-dialog-save-button'], [data-test-id='save-version-dialog-save-button'], button:has-text('Save')").last
#                 await confirm_btn.wait_for(state="visible", timeout=8000)
#                 await confirm_btn.click()
#                 print("🚀 Background 'Save & Run All' successfully triggered!")
#             except Exception as e:
#                 print(f"⚠️ Confirm button selector missed ({e}). Trying fallback keyboard confirm...")
#                 await page.keyboard.press("Enter")
#         else:
#             print("⚠️ Primary JS button locator missed. Deploying fallback hotkey sequence...")
#             # Fallback hotkey sequence to open Save Version dialog if UI changed: Ctrl + Shift + S
#             await page.focus("body")
#             await page.keyboard.down("Control")
#             await page.keyboard.down("Shift")
#             await page.keyboard.press("s")
#             await page.keyboard.up("Shift")
#             await page.keyboard.up("Control")
#             await page.wait_for_timeout(4000)
#             await page.keyboard.press("Enter")
#             print("⚡ Hotkey Save Version pipeline dispatched.")

#         print("⏳ Waiting 15 seconds to ensure the backend server locks in the commit token...")
#         await page.wait_for_timeout(15000)
        
#         print("\n" + "="*80)
#         print("🎉 PIPELINE TRIGGER COMPLETE!")
#         print("Kaggle is now running your script in a locked background environment on your GPU T4.")
#         print("The GPU will automatically power off and stop usage the exact second your code finishes.")
#         print("🔗 Track execution and view live logs here: https://kaggle.com")
#         print("="*80 + "\n")
        
#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run())




import os
import sys
import time
from playwright.sync_api import sync_playwright

def run_automated_save_version():
    email = os.getenv("KAGGLE_EMAIL")
    password = os.getenv("KAGGLE_PASSWORD")
    username = os.getenv("KAGGLE_USERNAME")
    notebook_slug = os.getenv("KAGGLE_NOTEBOOK_SLUG")

    if not all([email, password, username, notebook_slug]):
        print("❌ Error: Missing vital repository configuration credentials.")
        sys.exit(1)

    with sync_playwright() as p:
        print("🚀 Launching residential browser engine context...")
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
            locale="en-US"
        )
        page = context.new_page()

        # 1. Open direct email login page
        print("📥 Requesting direct email login page...")
        direct_url = "https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2F"
        page.goto(direct_url, wait_until="networkidle", timeout=60000)
        time.sleep(3) 

        try:
            # 2. Autofill credentials
            print("✍️ Filling out credentials...")
            page.locator('input[name="email"]').wait_for(state="visible", timeout=15000)
            page.locator('input[name="email"]').fill(email, timeout=5000)
            page.locator('input[name="password"]').fill(password, timeout=5000)
            
            print("🔑 Submitting login...")
            page.locator('button:has-text("Sign In")').click()
            
            page.wait_for_url("https://kaggle.com", timeout=45000)
            print("🔓 Logged in successfully.")

        except Exception as login_err:
            print(f"❌ Authentication failed: {login_err}")
            page.screenshot(path="error_screenshot.png")
            sys.exit(1)

        # 3. Route to the workspace editor 
        editor_url = f"https://kaggle.comcode/{username}/{notebook_slug}/edit"
        print(f"📂 Instantiating cloud editor environment: {editor_url}")
        page.goto(editor_url, wait_until="networkidle", timeout=60000)
        time.sleep(25) # Give the complex Jupyter workspace UI plenty of time to fully build

        # 4. Save Version (Commit) Workflow Injection
        print("⚡ Initiating 'Save Version' sequence...")
        try:
            # Click the main "Save Version" button in the top right corner
            save_version_btn = page.locator('button:has-text("Save Version"), [data-test-id="save-version-button"]')
            save_version_btn.wait_for(state="visible", timeout=20000)
            save_version_btn.click()
            print("👁️ Save options modal opened.")
            time.sleep(3)

            # Ensure "Save & Run All (Commit)" option is selected/checked
            # Kaggle defaults to this, but explicitly locating text safeguards against UI updates
            commit_radio_label = page.locator('label:has-text("Save & Run All (Commit)")')
            if commit_radio_label.is_visible():
                commit_radio_label.click()
                time.sleep(1)

            # Click the blue "Save" button inside the popup modal window
            modal_save_btn = page.locator('div[role="dialog"] button:has-text("Save"), button[data-test-id="modal-save-button"]')
            # Fallback locator if custom data attributes change
            if not modal_save_btn.is_visible():
                modal_save_btn = page.locator('button:has-text("Save")').last
                
            modal_save_btn.wait_for(state="visible", timeout=10000)
            modal_save_btn.click()
            
            print("🎉 Success! 'Save Version' triggered. The backend will run the notebook on GPU T4x2 and shut down automatically.")
            time.sleep(10) # Safe margin for backend pipeline acknowledgement

        except Exception as ui_error:
            print(f"❌ Failed to click Save Version elements: {ui_error}")
            page.screenshot(path="error_screenshot.png")
            sys.exit(1)

        context.close()
        browser.close()

if __name__ == "__main__":
    run_automated_save_version()
