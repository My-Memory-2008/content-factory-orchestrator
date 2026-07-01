import os
import cv2
import json
import base64
from openai import OpenAI

# Connect directly to the local Ollama background engine service
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" # String required by client validation, ignored by local daemon
)

# Target the vision-language model pulled in your workflow setup
MODEL_NAME = "qwen2.5-vl:3b"

def analyze_frames_via_qwen_local(b64_frames):
    """Sends the frame pipeline to local Ollama Qwen2.5-VL engine for metric sorting."""
    if not b64_frames:
        return False

    content_payload = [
        {
            "type": "text",
            "text": (
                "Analyze this sequence of video frames extracted from an Instagram Reel.\n"
                "Evaluate these three specific metrics precisely:\n"
                "1. Is there any visible text watermark, platform logo, or custom username overlay?\n"
                "2. Is this a 'faceless' reel? (Return True if there are NO human faces visible, False if human faces appear).\n"
                "3. Is there any obvious product promotion, brand placement, or creator advertisement?\n\n"
                "Respond ONLY in this exact raw JSON schema structure, with no markdown tags and no explanations:\n"
                '{\n  "has_watermark": true,\n  "is_faceless": true,\n  "has_promotion": true\n}'
            )
        }
    ]
    
    # Inject images into the prompt structure
    for img_b64 in b64_frames:
        content_payload.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{img_b64}"
            }
        })

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": content_payload}],
            model=MODEL_NAME,
            temperature=0.1
        )
        
        raw_text = response.choices.message.content.strip()
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()
        result = json.loads(clean_text)
        
        print(f"Local Qwen Evaluation Result: {result}")
        
        if not result.get("has_watermark") and result.get("is_faceless") and not result.get("has_promotion"):
            return True
        return False
        
    except Exception as e:
        print(f"Ollama local inference exception occurred: {e}")
        return False
