import modal
import os, time

GPU_TYPE = os.environ.get("GPU_TYPE", "T4") #NEW
app = modal.App("comfyui-antique")
vol = modal.Volume.from_name("workspace", create_if_missing=True)

def install_comfyui_dependencies():
    os.system("cd /root/workspace/ComfyUI && uv pip install --system -r requirements.txt")
    os.system("cd /root/workspace/ComfyUI/custom_nodes/ComfyUI-Manager && uv pip install --system -r requirements.txt")
    os.system("python /root/workspace/ComfyUI/custom_nodes/ComfyUI-Manager/cm-cli.py restore-dependencies")
    
image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("git", "wget", "curl", "aria2", "libgl1", "lsof", "libglib2.0-0", "unzip")
    .pip_install("jupyterlab", "notebook", "ipykernel", "numpy", "pandas", "matplotlib", "seaborn", "gdown")
    .run_commands(
        "mkdir -p /root/.jupyter/lab/user-settings/@jupyterlab/apputils-extension",
        'echo \'{"theme": "JupyterLab Dark"}\' > /root/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings',
        "chmod 755 /root",
        "wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared && chmod +x cloudflared && mv cloudflared /usr/local/bin/",
        # "",
    )
    
    .run_function(
        install_comfyui_dependencies,
        volumes={"/root/workspace": vol}
    )
)

@app.function(
    image=image,
    gpu=GPU_TYPE,
    timeout=24*3600,  # 24 hour
    volumes={"/root/workspace": vol},
)
def run():
    os.system("jupyter lab --ip=0.0.0.0 --port=5000 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' &")
    time.sleep(5)
    os.system("cd /root/workspace/ComfyUI && python main.py --listen 0.0.0.0 --port 8188 &")
    time.sleep(10)
    os.system("cloudflared tunnel run tensorart")
    print("Starting ComfyUI...✅")

  

