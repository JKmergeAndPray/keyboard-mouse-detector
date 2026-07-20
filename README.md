# Keyboard & Mouse Detector - YOLO11 Segmentation Deployment

A computer vision application that detects and segments computer peripherals using a custom-trained YOLO11 segmentation model.

The project demonstrates the complete machine learning deployment workflow:

- Model training with YOLO11
- Model inference
- Flask web application
- Docker containerization
- Local deployment

---

## Project Overview

The application allows users to upload an image of a computer setup and automatically detects:

- Computer Mouse
- Keyboard

The YOLO segmentation model returns the detected objects with bounding boxes, labels, and segmentation masks.

---

## Demo

Upload an image:

User Image

↓

Flask Web Application

↓

YOLO11 Segmentation Model

↓

Detected Objects

Example output:

- Computer Mouse detected
- Keyboard detected
- Confidence scores displayed by YOLO

---

## Technologies Used

### Machine Learning
- YOLO11 Segmentation
- Ultralytics
- PyTorch

### Backend
- Python
- Flask

### Deployment
- Docker
- Docker Image
- Containerized inference service

### Computer Vision
- OpenCV
- NumPy

---

## Project Structure

Keyboard_Mouse_Detector_Deployment/

├── app.py # Flask application

├── best.pt # Trained YOLO segmentation model

├── requirements.txt # Python dependencies

├── Dockerfile # Docker configuration

├── .dockerignore # Files excluded from Docker build

├── templates/
│ └── index.html # Web interface

├── static/
│ ├── style.css # Frontend styling
│ ├── uploads/ # Uploaded images
│ └── results/ # Prediction outputs


---

# Running the Project Locally

## 1. Clone the repository

```bash
git clone <repository-url>

cd Keyboard_Mouse_Detector_Deployment

## 2. Create virtual environment

```bash
python -m venv venv

### Activate it

```bash
venv\Scripts\activate

## Install dependencies

```bash
pip install -r requirements.txt

## Run Flask application

```bash
python app.py

(The application will run at: http://127.0.0.1:5000)


---


# Running with Docker

## Build Docker image

```bash
docker build -t keyboard-mouse-detector .

## Run container

```bash
docker run -p 5000:5000 keyboard-mouse-detector

-> Lastly open your local host

---

# Model Information

Model: YOLO11n-seg
Task: Instance Segmentation
Classes: 0: Computer Mouse - 1: Keyboard

---

# Inference Pipeline

1. User uploads image
2. Flask saves uploaded file
3. YOLO11 performs inference
4. Detection masks and labels are generated
5. Result image is returned to the user

---

#Future Improvements

##Possible improvements:
Augment the Dataset
Improve frontend design
Add automated testing
Add REST API endpoint

---

Author

Jean Keshishian