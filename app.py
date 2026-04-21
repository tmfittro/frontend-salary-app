from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_url = "https://colbert-salary-api-cgawbyc6fah3b0g8.eastus-01.azurewebsites.net/predict"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = {
        "age": 7,
        "gender": 0,
        "country": 55,
        "highest_deg": 3,
        "coding_exp": 4,
        "title": 13
    }

    try:
        r = requests.post(api_url, json=data)
        result = r.json()
        prediction = result.get("prediction") or result.get("error")
    except:
        prediction = "API connection error"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5002)