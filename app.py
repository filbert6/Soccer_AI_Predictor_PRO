from flask import Flask, request, jsonify
from scraper_365scores import scrape_match
from ensemble import predict_match

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    url = request.json.get("url")
    match_data = scrape_match(url)
    prediction = predict_match(match_data)
    return jsonify({"match": match_data, "prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
