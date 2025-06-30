# ML-Digit-classifier-classical /
# Handwritten Digit Recognizer (Classical ML)
The purpose of this project was make basic operations in docker.
This is a lightweight web app that uses a classical machine learning model (Random Forest) to recognize handwritten digits. Built with Flask and Docker.

Features

- Draw digits using an in-browser canvas
- Real-time prediction using scikit-learn
- Dockerized and ready for deployment
- Classical ML — no TensorFlow or deep learning

## Model

- Trained on sklearn.datasets.load_digits() (8×8 grayscale digits)
- Uses RandomForestClassifier

## Interface

- Minimal TailwindCSS-based design
- Canvas for drawing input
- Prediction shown instantly

## Run with Docker

```bash
docker build -t digit-app .
docker run -p 5000:5000 digit-app
