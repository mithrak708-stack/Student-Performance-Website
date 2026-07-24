from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load ML model
model = joblib.load("model.pkl")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Services Page
@app.route("/services")
def services():
    return render_template("services.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    try:
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        previous_score = float(request.form["previous_score"])
        sleep_hours = float(request.form["sleep_hours"])
        papers = float(request.form["papers"])

        prediction = model.predict(
            [[hours, attendance, previous_score, sleep_hours, papers]]
        )[0]

        # Limit prediction between 0 and 100
        prediction = max(0, min(100, prediction))
        prediction = round(prediction, 2)

        # Grade
        if prediction >= 90:
            grade = "A+"
            status = "Excellent"

        elif prediction >= 80:
            grade = "A"
            status = "Very Good"

        elif prediction >= 70:
            grade = "B"
            status = "Good"

        elif prediction >= 60:
            grade = "C"
            status = "Average"

        elif prediction >= 50:
            grade = "D"
            status = "Needs Improvement"

        else:
            grade = "F"
            status = "Poor"


        return render_template(
            "index.html",
            prediction=prediction,
            grade=grade,
            status=status
        )


    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)