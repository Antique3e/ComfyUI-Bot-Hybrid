"""
Modal Setup Step 1
==================
ADD YOUR SETUP CODE HERE

This is the first step of the setup process.
Run with: modal run app1.py::run

Timeout: 2 hours
GPU: Configurable (set via GPU_TYPE environment variable)

Example tasks for Step 1:
- Clone repositories
- Download large model files
- Initial workspace setup
- Install system dependencies

INSTRUCTIONS:
1. Keep the app.function decorator
2. Keep the run() function name
3. Add your code inside the run() function
4. Use GPU_NAME placeholder - bot will replace it with actual GPU
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

app = modal.App("setup-step1")
vol = modal.Volume.from_name("workspace", create_if_missing=True)

# ============================================================================
# IMAGE DEFINITION
# ============================================================================

# Define your image with required dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("git", "wget", "curl")
    # Add more dependencies as needed
)

# ============================================================================
# SETUP STEP 1 FUNCTION
# ============================================================================

@app.function(
    image=image,
    gpu=GPU_NAME,  # ← This will be replaced by bot with actual GPU (H100, A100, etc.)
    timeout=7200,  # 2 hours
    volumes={"/root/workspace": vol},
)
def run():
    """
    Setup Step 1 - Add your code here
    
    This function will be called by the Discord bot using:
    GPU_TYPE=H100 modal run app1.py::run
    """
    
    print("=" * 80)
    print("SETUP STEP 1 - START")
    print("=" * 80)
    print(f"GPU: {GPU_TYPE}")
    print("=" * 80)
    
    # ========================================
    # ADD YOUR SETUP CODE BELOW
    # ========================================
    
    # Example:
    # print("\n[1/3] Cloning repository...")
    # os.system("git clone https://github.com/your-repo /root/workspace/repo")
    
    # print("\n[2/3] Downloading models...")
    # os.system("wget https://example.com/model.safetensors -P /root/workspace/models")
    
    # print("\n[3/3] Installing dependencies...")
    # os.system("pip install -r /root/workspace/requirements.txt")
    
    print("\n⚠️  SETUP STEP 1 CODE NOT ADDED YET")
    print("Please add your setup code in app1.py")
    
    # ========================================
    # END OF YOUR CODE
    # ========================================
    
    print("\n" + "=" * 80)
    print("✅ SETUP STEP 1 - COMPLETE!")
    print("=" * 80)

# ============================================================================
# END OF SETUP STEP 1
# ============================================================================
