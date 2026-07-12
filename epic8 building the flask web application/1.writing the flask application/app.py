from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model/HDI.pkl", "rb"))


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("home.html")


# -----------------------------
# Prediction Page
# -----------------------------
@app.route("/Prediction")
def prediction():
    return render_template("indexnew.html")


# -----------------------------
# Predict HDI
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    # Read form values
    country = request.form["country"]
    life = float(request.form["life"])
    schooling = float(request.form["schooling"])
    gni = float(request.form["gni"])
    internet = float(request.form["internet"])

    # Create DataFrame
    data = pd.DataFrame(
        [[life, schooling, gni, internet]],
        columns=[
            "Life Expectancy",
            "Schooling",
            "GNI per Capita",
            "Internet Users (%)"
        ]
    )

    # Predict HDI
    prediction = model.predict(data)

    return render_template(
        "resultnew.html",
        country=country,
        prediction_text=f"Predicted HDI : {prediction[0]:.3f}"
    )


if __name__ == "__main__":
    app.run(debug=True)