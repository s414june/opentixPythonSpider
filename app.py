from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_results = searchOpentix(data)
    return jsonify(search_results)

@app.errorhandler(ValueError)
def handle_value_error(error):
    response = jsonify({"error": str(error)})
    response.status_code = 400
    return response

@app.errorhandler(500)
def handle_internal_server_error(error):
    response = jsonify({"error": "An unexpected error occurred"})
    response.status_code = 500
    return response

def searchOpentix(query):
    url = 'https://search.opentix.life/search'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = query

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
