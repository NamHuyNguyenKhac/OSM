import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fetch_parks')
def fetch_parks():
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = """
    [out:json];
    area[name="HaNoi"]->.searchArea;
    node["leisure"="park"](area.searchArea);
    out body;
    """
    response = requests.get(overpass_url, params={'data': query})
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
