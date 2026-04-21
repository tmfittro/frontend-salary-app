@app.route("/predict", methods=["POST"])
def predict():
    try:
        # build JSON EXACTLY how API wants it
        data = {
            "age": int(request.form["age"]),
            "gender": int(request.form["gender"]),
            "country": int(request.form["country"]),
            "highest_deg": int(request.form["highest_deg"]),
            "coding_exp": int(request.form["coding_exp"]),
            "title": int(request.form["title"])
        }

        # 🔥 FORCE correct headers
        response = requests.post(
            api_url,
            json=data,
            headers={"Content-Type": "application/json"}
        )

        print("SENT:", data)
        print("RESPONSE:", response.text)

        result = response.json()

        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {e}")