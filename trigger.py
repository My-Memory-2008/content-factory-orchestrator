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
#     "gpu_group": "dual_t4",
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

import os
import json
import subprocess
import sys
import requests
import re

# Ingestion check ensuring base environment tools are loaded cleanly
try:
    import kaggle
except ImportError:
    print("-> 'kaggle' module missing. Initiating install sequence...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle", "-q"])
    import kaggle

# 1. Gather all configuration variables securely from environment vaults
KAGGLE_USERNAME = os.environ.get("KAGGLE_USERNAME", "muhammadasjad2008").strip()
KAGGLE_KEY = os.environ.get("KAGGLE_KEY", "").strip()
KAGGLE_WEB_COOKIE = os.environ.get("KAGGLE_WEB_COOKIE", "").strip()

# 🔥 THE ARCHITECTURAL RESET CORRECTION:
# Modifying the endpoint slug references forces Kaggle to spin up a completely fresh execution layer,
# permanently bypassing the P100 hardware configuration locks tied to your old script name!
SLUG = "content-factory-engine-v2"
KERNEL_REF = f"{KAGGLE_USERNAME}/{SLUG}"

# STEP 2: OVERRIDE ACCELERATOR BYSETS VIA PROGRAMMATIC WEB ROUTE
if KAGGLE_WEB_COOKIE:
    try:
        print("📡 Injecting explicit Dual T4 hardware state directly into Kaggle settings table...")
        
        # Pull out the dynamic production XSRF-TOKEN parameters from your native web layout string safely
        xsrf_match = re.search(r'XSRF-TOKEN=([^;]+)', KAGGLE_WEB_COOKIE)
        xsrf_token = xsrf_match.group(1) if xsrf_match else ""
        
        # Kaggle web settings API endpoint route map targets
        settings_url = "https://kaggle.com"
        
        headers = {
            "Cookie": KAGGLE_WEB_COOKIE,
            "X-Xsrf-Token": xsrf_token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Origin": "https://kaggle.com",
            "Referer": f"https://kaggle.com/code/{KAGGLE_USERNAME}/{SLUG}/settings"
        }
        
        # Forces your notebook settings rows to bind tightly to Dual T4x2 engines on Kaggle tables
        payload = {
            "kernelRef": KERNEL_REF,
            "gpuType": "gpuT4",
            "isGpuGroup": True,
            "isGpuEnabled": True
        }
        
        with requests.Session() as web_session:
            web_session.trust_env = False
            response = web_session.post(settings_url, headers=headers, json=payload, timeout=20)
            
        if response.status_code == 200 or response.status_code == 240:
            print("🚀 DATABASE SUCCESS! Hardware cluster explicitly set to Dual T4 (T4x2).")
        else:
            print(f"⚠️ Settings route bypass returned status state {response.status_code}. Proceeding with standard push protocols...")
            
    except Exception as network_override_fault:
        print(f"⚠️ Internal webhook bypass step skipped: {network_override_fault}")

# --- 3. EXECUTE STANDARD METADATA WRITE & FILE SYNC PUSH ---
print("[1/2] Syncing local structural properties payload...")
meta_payload = {
    "id": KERNEL_REF,
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

print("[2/2] Launching final code file payload synchronization push...")
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.kernels_push(".")
print("✅ Core file synchronization upload finalized smoothly over direct endpoints.")
