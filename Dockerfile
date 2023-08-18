# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the script and requirements file into the container at /app
COPY prediction.py .
COPY requirements.txt .

# Copy the trained model file into the container at /app
COPY best.pt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install git and other dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the YOLOv5 repository
RUN git clone https://github.com/ultralytics/yolov5.git

# Perform cleanup and remove .github directory
RUN rm -rf /app/yolov5/.github


# Define the command to run your application
CMD ["uvicorn", "prediction]
