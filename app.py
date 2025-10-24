"""
Modal ComfyUI Runtime
=====================
ADD YOUR RUNTIME CODE HERE

This is the main runtime file for starting ComfyUI.
Run with: modal run app.py::run

Timeout: 24 hours
GPU: Configurable (set via GPU_TYPE environment variable)

Example tasks for Runtime:
- Start JupyterLab
- Start ComfyUI
- Start Cloudflare tunnel
- Keep services running

INSTRUCTIONS:
1. Keep the app.function decorator
2. Keep the run() function name
3. Add your code inside the run() function
4. Use GPU_NAME placeholder - bot will replace it with actual GPU
5. This should START services and keep them running
6. Last command should be blocking (like cloudflared tunnel run)
"""

import modal
import os
import time

# ============================================================================
# GPU SELECTION
# ============================================================================

# Get GPU from environment variable (set by Discord bot)
GPU_TYPE = os.environ.get("GPU_TYPE", "GPU_NAME")

print(f"🖥️  Selected GPU: {GPU_TYPE}")

# ============================================================================
# MODAL APP CONFIGURATION
# ============================================================================

app = modal.App("comfyui-runtime")
vol = modal.Volume.from_name("workspace", create_if_missing=True)

# ============================================================================
# IMAGE DEFINITION
# ============================================================================

# Define your image with required dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install(
        "git",
        "wget",
        "curl",
        "python3-pip",
    )
    .pip_install(
        "jupyterlab",
        "notebook",
    )
    # Add more dependencies as needed
)

# ============================================================================
# RUNTIME FUNCTION
# ============================================================================

@app.function(
    image=image,
    gpu=GPU_NAME,  # ← This will be replaced by bot with actual GPU (H100, A100, etc.)
    timeout=86400,  # 24 hours
    volumes={"/root/workspace": vol},
)
def run():
    """
    ComfyUI Runtime - Add your code here
    
    This function will be called by the Discord bot using:
    GPU_TYPE=H100 modal run app.py::run
    
    This should:
    1. Start JupyterLab (background)
    2. Start ComfyUI (background)
    3. Start Cloudflare tunnel (blocking - keeps container running)
    """
    
    print("=" * 80)
    print("COMFYUI RUNTIME - START")
    print("=" * 80)
    print(f"GPU: {GPU_TYPE}")
    print("=" * 80)
    
    # ========================================
    # ADD YOUR RUNTIME CODE BELOW
    # ========================================
    
    # Example:
    # print("\n[1/4] Installing Cloudflare tunnel...")
    # os.system("wget cloudflared... && chmod +x cloudflared && mv cloudflared /usr/local/bin/")
    
    # print("\n[2/4] Starting JupyterLab...")
    # os.system("jupyter lab --ip=0.0.0.0 --port=5000 --no-browser --allow-root --NotebookApp.token='' &")
    # time.sleep(5)
    
    # print("\n[3/4] Starting ComfyUI...")
    # os.system("cd /root/workspace/ComfyUI && python main.py --listen 0.0.0.0 --port=8188 &")
    # time.sleep(5)
    
    # print("\n[4/4] Starting Cloudflare tunnel (keeps container running)...")
    # os.system("cloudflared tunnel run your-tunnel-name")
    
    print("\n⚠️  RUNTIME CODE NOT ADDED YET")
    print("Please add your ComfyUI start code in app.py")
    print("\n💡 Remember: Last command should be blocking (cloudflared tunnel)")
    
    # Keep alive for testing (remove this when you add your code)
    print("\n⏳ Keeping container alive for 60 seconds (for testing)...")
    time.sleep(60)
    
    # ========================================
    # END OF YOUR CODE
    # ========================================
    
    print("\n" + "=" * 80)
    print("✅ COMFYUI RUNTIME - STOPPED")
    print("=" * 80)

# ============================================================================
# END OF RUNTIME
# ============================================================================
