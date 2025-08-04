from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

# Ensure folder exists
PHOTO_FOLDER = os.path.join("static", "captured")
os.makedirs(PHOTO_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/capture", methods=["POST"])
def capture():
    photo = request.files.get("photo")
    if photo:
        filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")
        photo_path = os.path.join(PHOTO_FOLDER, filename)
        photo.save(photo_path)
        return "Photo saved", 200
    return "No photo received", 400

if __name__ == "__main__":
    app.run(debug=True)