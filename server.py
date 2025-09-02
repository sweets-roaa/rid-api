from flask import Flask, request, jsonify

app = Flask(__name__)

latest_rid = None  # نخزّن آخر RID هنا

@app.route('/save_rid', methods=['POST'])
def save_rid():
    global latest_rid
    data = request.get_json()
    if not data or "rid" not in data:
        return jsonify({"error": "No RID received"}), 400

    latest_rid = data["rid"]
    print(f"[✅] RID updated: {latest_rid}")
    return jsonify({"status": "RID saved", "rid": latest_rid}), 200


@app.route('/get_rid', methods=['GET'])
def get_rid():
    if latest_rid is None:
        return jsonify({"error": "No RID found"}), 404
    return jsonify({"rid": latest_rid}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
