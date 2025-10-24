"""
Modal Setup Step 2
==================
ADD YOUR SETUP CODE HERE

This is the second step of the setup process.
Run with: modal run app2.py::run

Timeout: 20 minutes
GPU: Configurable (set via GPU_TYPE environment variable)

Example tasks for Step 2:
- Install Python dependencies
- Configure ComfyUI custom nodes
- Install additional packages
- Finalize setup (NO JUPYTER/COMFYUI START)

IMPORTANT: Do NOT start JupyterLab or ComfyUI here!
           Only install dependencies and configure.

INSTRUCTIONS:
1. Keep the app.function decorator
2. Keep the run() function name
3. Add your code inside the run() function
4. Use GPU_NAME placeholder - bot will replace it with actual GPU
5. DO NOT start JupyterLab or ComfyUI services
"""

import modal
import os

# ============================================================================
# GPU SELECTION
# ============================================================================

# Get GPU from environment variable (set by Discord bot)
GPU_TYPE = os.environ.get("GPU_TYPE", "GPU_NAME")

print(f"🖥️  Selected GPU: {GPU_TYPE}")

# ============================================================================
# MODAL APP CONFIGURATION
# ============================================================================

app = modal.App("setup-step2")
vol = modal.Volume.from_name("workspace", create_if_missing=True)

# ============================================================================
# IMAGE DEFINITION
# ============================================================================

# Define your image with required dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("git", "wget", "curl", "python3-pip")
    # Add more dependencies as needed
)

# ============================================================================
# SETUP STEP 2 FUNCTION
# ============================================================================

@app.function(
    image=image,
    gpu=GPU_NAME,  # ← This will be replaced by bot with actual GPU (H100, A100, etc.)
    timeout=1200,  # 20 minutes
    volumes={"/root/workspace": vol},
)
def run():
    """
    Setup Step 2 - Add your code here
    
    This function will be called by the Discord bot using:
    GPU_TYPE=H100 modal run app2.py::run
    
    IMPORTANT: Only install dependencies, do NOT start services!
    """
    
    print("=" * 80)
    print("SETUP STEP 2 - START")
    print("=" * 80)
    print(f"GPU: {GPU_TYPE}")
    print("=" * 80)
    
    # ========================================
    # ADD YOUR SETUP CODE BELOW
    # ========================================
    
    # Example:
    # print("\n[1/4] Installing ComfyUI requirements...")
    # os.system("pip install -r /root/workspace/ComfyUI/requirements.txt")
    
    # print("\n[2/4] Installing custom node dependencies...")
    # os.system("pip install some-package another-package")
    
    # print("\n[3/4] Configuring settings...")
    # os.system("echo 'config=value' > /root/workspace/config.txt")
    
    # print("\n[4/4] Finalizing setup...")
    # os.system("touch /root/workspace/.setup_complete")
    
    print("\n⚠️  SETUP STEP 2 CODE NOT ADDED YET")
    print("Please add your dependency installation code in app2.py")
    print("\n⚠️  REMEMBER: Do NOT start JupyterLab or ComfyUI here!")
    
    # ========================================
    # END OF YOUR CODE
    # ========================================
    
    print("\n" + "=" * 80)
    print("✅ SETUP STEP 2 - COMPLETE!")
    print("=" * 80)
    print("🎉 Setup finished! You can now use /start to run ComfyUI")

# ============================================================================
# END OF SETUP STEP 2
# ============================================================================
