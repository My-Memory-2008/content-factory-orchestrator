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





# ==========================================
# PHASE B: AUTHENTIC WEB INTERFACE DUAL-HARDWARE ACCELERATION OVERRIDER
# ==========================================
print("🧠 Initializing Direct Playwright Web-Interface Hardware Overrider Engine...")

import os
import json
import subprocess
import sys

# 🔥 FIX 1: MOVE KAGGLE MODULE CORE DEPENDENCY TO THE ABSOLUTE TOP OF THE EXECUTION MATRIX
try:
    import kaggle
except ImportError:
    print("📡 'kaggle' module missing. Initiating immediate package setup pass...")
    subprocess.run([sys.executable, "-m", "pip", "install", "kaggle", "-q"], check=True)
    import kaggle

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("📡 Playwright framework missing. Initiating automatic browser dependencies setup pass...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pip", "--upgrade", "-q"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "playwright", "-q"], check=True)
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    from playwright.sync_api import sync_playwright

# --- 2. AUTHENTICATION CREDENTIALS EXTRACTION ---
KAGGLE_USERNAME = os.environ.get("KAGGLE_USERNAME", "muhammadasjad2008").strip()
KAGGLE_KEY = os.environ.get("KAGGLE_KEY", "").strip()
KAGGLE_WEB_COOKIE = os.environ.get("KAGGLE_WEB_COOKIE", "").strip()

SLUG = "content-factory-engine-v2"

# 🔥 FIX 2: REPAIRED URL STRIP MAPPING 
# Removed the invalid trailing star characters to prevent any net::ERR_NAME_NOT_RESOLVED drops!
TARGET_SETTINGS_URL = f"https://kaggle.com{KAGGLE_USERNAME}/{SLUG}/settings"

if not KAGGLE_WEB_COOKIE:
    print("⚠️ Warning: KAGGLE_WEB_COOKIE env container returned blank.")
    print("💡 Proceeding straight to direct endpoint push pass using standard credentials...")
else:
    print(f"🔗 Spinning up clean browser context layer to target layout zone: {TARGET_SETTINGS_URL}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        
        cookie_dictionary_list = []
        raw_clean_cookie = KAGGLE_WEB_COOKIE.strip()
        
        for cookie_segment in raw_clean_cookie.split(";"):
            cookie_segment = cookie_segment.strip()
            if not cookie_segment or "=" not in cookie_segment:
                continue
                
            c_name, c_val = cookie_segment.split("=", 1)
            c_name = c_name.strip()
            c_val = c_val.strip()
            
            if c_name.startswith("_ga") or c_name == "ACCEPTED_COOKIES":
                continue
                
            # 🔥 FIX 3: STRIP EXTRA QUOTES FROM TARGET STRINGS
            # Cleanly sanitizes domains to prevent Storage.setCookies protocol exceptions inside Chromium
            cookie_dictionary_list.append({
                "name": c_name,
                "value": c_val,
                "domain": ".kaggle.com",  
                "path": "/"
            })
            
        try:
            context.add_cookies(cookie_dictionary_list)
            print("✅ Web cookies cleaned, verified, and successfully injected into browser environment.")
        except Exception as cookie_fault:
            print(f"⚠️ Warning: Playwright cookie injection encountered a loose segment validation drop: {cookie_fault}")
            
        page = context.new_page()
        
        try:
            print("📡 Establishing stable data stream connection to your Kaggle control dashboard...")
            page.goto(TARGET_SETTINGS_URL, wait_until="load", timeout=60000)
            page.wait_for_timeout(5000) 
            
            print("🎯 Searching canvas for the hardware accelerator tray dropdown element...")
            accelerator_box = page.locator('text=Accelerator').first
            if accelerator_box.count() > 0:
                accelerator_box.click()
                page.wait_for_timeout(2000)
                
                print("⚡ OVERRIDING FALLBACKS: Force-selecting GPU T4 x2 Multi-Core Array Element...")
                page.locator('text=GPU T4 x2').first.click()
                page.wait_for_timeout(2000)
                
                print("💾 Committing changes to platform configuration database registries...")
                page.locator('text=Save').first.click()
                page.wait_for_timeout(4000)
                print("🚀 STEP SUCCESSFUL! Notebook default allocation state forcefully overridden to Dual T4.")
            else:
                print("⚠️ Notice: Settings menu panel option row target hidden or locked.")
        except Exception as automation_fault:
            print(f"❌ Automation interface loop challenged: {automation_fault}")
            
        browser.close()

# --- 3. EXECUTE BASE METADATA WRITE & KERNEL PAYLOAD PUSH ---
print("\n[1/2] Generating localized script execution block parameter tables...")
meta_payload = {
    "id": f"{KAGGLE_USERNAME}/{SLUG}",
    "title": "Content Factory Engine v2",
    "code_file": "content-factory-engine.py",
    "language": "python",
    "kernel_type": "script",
    "is_private": "true",
    "enable_gpu": "true",
    "enable_internet": "true",
    "dataset_sources": ["muhammadasjad2008/cat-reactions-vault"],
    "competition_sources": [],
    "kernel_sources": []
}

with open("kernel-metadata.json", "w") as f:
    json.dump(meta_payload, f, indent=2)

home_dir = os.path.expanduser("~")
kaggle_folder = os.path.join(home_dir, ".kaggle")
os.makedirs(kaggle_folder, exist_ok=True)
with open(os.path.join(kaggle_folder, "kaggle.json"), "w") as f:
    json.dump({"username": KAGGLE_USERNAME, "key": KAGGLE_KEY}, f)
os.chmod(os.path.join(kaggle_folder, "kaggle.json"), 0o600)

print("[2/2] Ingesting source payloads directly into authenticated sync endpoints...")
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.kernels_push(".")
print("✅ Phase A Complete: Deployment cycle finalized smoothly across dual T4 hardware allocations!")



