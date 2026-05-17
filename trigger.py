import os
import json
import requests

# 1. Pull credentials out of GitHub action runner environments
KAGGLE_USERNAME = os.environ.get("KAGGLE_USERNAME")
KAGGLE_KEY = os.environ.get("KAGGLE_KEY")

# Ensure fields don't accidentally contain whitespaces or newline tags
if KAGGLE_USERNAME: KAGGLE_USERNAME = KAGGLE_USERNAME.strip()
if KAGGLE_KEY: KAGGLE_KEY = KAGGLE_KEY.strip()

# Your precise lowercase user/slug identifier path
KERNEL_SLUG = "muhammadasjad2008/content-factory-engine"

# 2. Read the local execution chassis notebook script safely
if not os.path.exists("summa.py"):
    raise FileNotFoundError("❌ Critical Error: 'notebook.py' is missing from your repository root!")

with open("summa.py", "r", encoding="utf-8") as f:
    code_content = f.read()

# 3. Formulate the explicit payload parameters required by Kaggle's v1 REST engine
payload = {
    "id": 0,
    "slug": KERNEL_SLUG,
    "newTitle": "Content Factory Engine",
    "textCode": code_content,
    "language": "python",
    "kernelType": "notebook",
    "isPrivate": True,
    "enableGpu": True,
    "enableInternet": True,
    "datasetSources": [],
    "competitionSources": [],
    "kernel_sources": []
}

# 4. Fire the direct network POST payload over the cloud gateway
url = "https://kaggle.com"
auth = (KAGGLE_USERNAME, KAGGLE_KEY)

print(f"📡 Dispatching payload directly to Kaggle REST endpoint: {url}...")
response = requests.post(url, auth=auth, json=payload)

# 5. Safe Handshake Verification
print(f"📡 Response Status Received: HTTP {response.status_code}")

if response.status_code == 200:
    try:
        data = response.json()
        print(f"✅ SUCCESS! Kaggle GPU Engine Active. Executing Version: {data.get('versionNumber')}")
    except Exception as json_err:
        print("⚠️ Response returned HTTP 200 but payload body could not parse as JSON:")
        print(response.text)
else:
    print(f"❌ Handshake Denied by Kaggle Backend Server (HTTP {response.status_code})")
    print("📋 Diagnostic Server Output:")
    print("-" * 50)
    print(response.text) # Prints the actual raw HTML error description from Kaggle
    print("-" * 50)
    exit(1) # Fail the GitHub workflow cleanly with explicit reasons listed
