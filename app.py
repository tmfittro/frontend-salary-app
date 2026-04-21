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
        "age": int(request.form["age"]),
        "gender": int(request.form["gender"]),
        "country": int(request.form["country"]),
        "highest_deg": int(request.form["highest_deg"]),
        "coding_exp": int(request.form["coding_exp"]),
        "title": int(request.form["title"])
    }

    try:
        response = requests.post(api_url, json=data)
        result = response.json()
        prediction = result.get("prediction") or result.get("error")
    except:
        prediction = "API error"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)