import os
import subprocess
import shutil


def git_clone(repo_url="https://github.com/ultralytics/yolov5.git"):
    try:
        if not os.path.exists("yolov5"):
            current_dir = os.getcwd()
            subprocess.run(["git", "init", current_dir])
            subprocess.run(["git", "clone", repo_url, f"{current_dir}/yolov5"])
            print("Repository cloned successfully.")
            github_dir = os.path.join("yolov5", ".github")
            if os.path.exists(github_dir):
                shutil.rmtree(github_dir)
        else:
            print("yolov5 directory available")
    except Exception as e:
        print(f"Error while cloning repository: {e}")


git_clone()
