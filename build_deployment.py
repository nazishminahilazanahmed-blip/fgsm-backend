# backend/build_deployment.py
import os
import zipfile
import subprocess
import sys

def create_deployment_package():
    print("Creating deployment package for AWS Lambda...")
    
    # Create deployment directory
    os.makedirs("deployment_package", exist_ok=True)
    
    # Copy Python files
    files_to_copy = ["app_fgsm.py", "lambda_handler.py"]
    for file in files_to_copy:
        if os.path.exists(file):
            os.system(f"cp {file} deployment_package/")
            print(f"Copied {file}")
    
    # Install dependencies
    print("Installing dependencies...")
    subprocess.run([
        sys.executable, "-m", "pip", "install",
        "-r", "requirements.txt",
        "--target", "deployment_package",
        "--platform", "manylinux2014_x86_64",
        "--implementation", "cp",
        "--python-version", "3.9",
        "--only-binary=:all:",
        "--upgrade"
    ], check=True)
    
    # Create ZIP file
    print("Creating ZIP file...")
    with zipfile.ZipFile('deployment_package.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("deployment_package"):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, "deployment_package")
                zipf.write(file_path, arcname)
    
    print(f"Deployment package created: deployment_package.zip")
    print(f"Size: {os.path.getsize('deployment_package.zip') / (1024*1024):.2f} MB")

if __name__ == "__main__":
    create_deployment_package()