from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import uuid
import shutil

app = Flask(__name__)

# Load trained model once when the app starts
model = YOLO("best.pt")

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No image uploaded."

    image = request.files["image"]

    if image.filename == "":
        return "No image selected."

    # Generate a unique filename
    filename = f"{uuid.uuid4()}_{image.filename}"

    upload_path = os.path.join(UPLOAD_FOLDER, filename)

    image.save(upload_path)

    # Run YOLO prediction
    results = model.predict(
        source=upload_path,
        conf=0.4,
        save=True,
        verbose=False,
        imgsz=320
    )

    print("Prediction folder contents:")
    print(os.listdir("runs/segment/predict"))

    # Locate YOLO's output image
    save_dir = results[0].save_dir
    predicted_image = os.path.join(save_dir, filename)

    final_image = os.path.join(RESULT_FOLDER, filename)

    shutil.copy(predicted_image, final_image)

    return render_template(
        "index.html",
        result_image=filename
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )