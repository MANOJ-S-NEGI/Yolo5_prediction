import os
from flask import Flask, request, jsonify, render_template
import subprocess
import shutil
import signal

app = Flask(__name__)

# Set a global variable to keep track of the prediction subprocess
prediction_process = None


@app.route('/', methods=['GET'])
def Home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def start_prediction():
    global prediction_process
    try:
        if prediction_process is None or prediction_process.poll() is not None:
            shutil.copy("best.pt", "yolov5")
            command = [
                "python", f"yolov5/detect.py", "--weights", "best.pt", "--img", "416", "--conf", "0.5", "--source",
                "0"]
            prediction_process = subprocess.Popen(command)
            return "Prediction Started!"
        else:
            return "Prediction already running!"
    except Exception as e:
        return f"An error occurred during prediction: {e}"


@app.route('/stop', methods=['POST'])
def stop_prediction():
    global prediction_process
    try:
        if prediction_process is not None and prediction_process.poll() is None:
            os.kill(prediction_process.pid, signal.SIGINT)
            prediction_process = None
            return "Prediction Stopped!"
        else:
            return "No prediction process running!"
    except Exception as e:
        return f"An error occurred while stopping prediction: {e}"


if __name__ == "__main__":
    app.run(debug=True)
