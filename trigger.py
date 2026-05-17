#!/usr/bin/env python3
# trigger.py - Trigger Kaggle notebook execution via official Python API
import os, sys, time
from kaggle.api.kaggle_api_extended import KaggleApi

def trigger_kaggle_execution(folder_path: str, kernel_id: str, max_wait_minutes: int = 30):
    """
    Push notebook config to Kaggle and optionally wait for completion.
    
    Args:
        folder_path: Path to folder containing kernel-metadata.json + code file
        kernel_id: "username/kernel-slug" format
        max_wait_minutes: Max time to wait for execution (0 = fire-and-forget)
    """
    print(f"🔐 Initializing Kaggle API client...")
    
    try:
        # Initialize and authenticate
        api = KaggleApi()
        api.authenticate()  # Reads ~/.kaggle/kaggle.json or env vars
        print("✅ Authentication successful")
        
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        print("💡 Ensure KAGGLE_USERNAME and KAGGLE_KEY are set in environment")
        print("💡 Or create ~/.kaggle/kaggle.json with valid credentials")
        return False
    
    try:
        # Push configuration (this TRIGGERS execution on existing notebooks)
        print(f"📤 Pushing configuration from '{folder_path}'...")
        response = api.kernels_push(folder_path)
        
        print("✅ Push successful!")
        print(f"🔗 Remote URL: {response.get('url', 'N/A')}")
        print(f"📊 Initial status: {response.get('status', 'N/A')}")
        
    except Exception as e:
        print(f"❌ Push failed: {e}")
        return False
    
    # Optional: Wait for execution to complete
    if max_wait_minutes > 0:
        print(f"⏳ Monitoring execution (timeout: {max_wait_minutes} mins)...")
        start_time = time.time()
        timeout_seconds = max_wait_minutes * 60
        
        while time.time() - start_time < timeout_seconds:
            try:
                status_info = api.kernels_status(kernel_id)
                status = status_info.get("status", "unknown")
                print(f"📊 [{int((time.time()-start_time)/60)}m] Status: {status}")
                
                if status in ["complete", "error", "cancelled"]:
                    print(f"✅ Execution finished with status: {status}")
                    return status == "complete"
                    
            except Exception as e:
                print(f"⚠️ Status check failed: {e}")
                
            time.sleep(30)  # Poll every 30 seconds
        
        print(f"⚠️ Timeout reached. Execution may still be running.")
        return True  # Not a hard failure
    
    return True

if __name__ == "__main__":
    # Configuration
    FOLDER_PATH = os.environ.get("KAGGLE_PUSH_FOLDER", "./kaggle_deploy")
    KERNEL_ID = os.environ.get("KAGGLE_KERNEL_ID", "muhammadasjad2008/content-factory-engine")
    WAIT_MINUTES = int(os.environ.get("KAGGLE_WAIT_MINUTES", "0"))  # 0 = fire-and-forget
    
    # Wait for GitHub-Kaggle sync to register the new pipeline_data.json
    sync_wait = int(os.environ.get("KAGGLE_SYNC_WAIT_SECONDS", "50"))
    print(f"⏳ Waiting {sync_wait}s for GitHub-Kaggle sync to register new data...")
    time.sleep(sync_wait)
    
    # Trigger execution
    success = trigger_kaggle_execution(FOLDER_PATH, KERNEL_ID, WAIT_MINUTES)
    
    # Exit with proper code for GitHub Actions
    sys.exit(0 if success else 1)
