from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/AdminDetails/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    url = f"https://bookingadmin-production.up.railway.app/AdminDetails/{path}"
    method = request.method.lower()
    headers = {'Content-Type': 'application/json'}
    data = request.get_json() if request.method in ['POST', 'PUT'] else None

    response = requests.request(method, url, headers=headers, json=data)
    if response.status_code != 200:
        return jsonify(error='Failed to retrieve data'), 500
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
