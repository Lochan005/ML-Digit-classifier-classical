
from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("models/digit_classifier.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        pixels = request.form.get("pixels")
        if pixels:
            img_array = np.array(eval(pixels)).reshape(1, -1)
            prediction = model.predict(img_array)[0]
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
