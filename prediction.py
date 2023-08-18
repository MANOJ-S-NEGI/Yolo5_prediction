import os
from fastapi import FastAPI, File, UploadFile
import uvicorn
import subprocess
import shutil


def git_clone(repo_url="https://github.com/ultralytics/yolov5.git"):
    try:
        if not os.path.exists("yolov5"):
            current_dir = os.getcwd()
            subprocess.run(["git", "init", current_dir])
            subprocess.run(["git", "clone", repo_url, f"{current_dir}/yolov5"])
            print("Repository cloned successfully.")
            if os.path.exists("yolov5/.github"):
                os.rmdir("yolov5/.github")
            else:
                pass

        else:
            print(f"yolov5 directory available")
    except subprocess.CalledProcessError:
        print("Error while cloning repository.")


app = FastAPI()


@app.get('/')
def read():
    diction = {
        "prediction_model_name": "Yolo5_object_detection_HandSign",
        "copy url": "http://127.0.0.1:8000/docs"
    }
    return diction


# shows the uploaded image with prediction as title as plot plt
@app.post("/prediction")
async def prediction():
    git_clone()
    shutil.copy("best.pt", "yolov5")

    command = [
        "python", f"yolov5/detect.py", "--weights", "best.pt", "--img", "416", "--conf", "0.5", "--source",
        "0"]
    subprocess.run(command)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)