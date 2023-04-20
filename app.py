from flask import Flask, request, jsonify
from connecton import addMonument
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/addmonument', methods=["POST"])
def add_monument():
    try:
        monument_name = request.json['name']
        monument_details = request.json['details']
        registration_fees = request.json['fees']
        image_url = request.json['image']
        coor_lat = request.json['lat']
        coor_long = request.json['long']
    except:
        return jsonify({"success": False, "message": "Invalid fields"}), 201

    try:
        addMonument(monument_name, monument_details,
                    registration_fees, image_url, coor_lat, coor_long)
        return jsonify({"success": True, "message": "Monument added successfully"}), 200
    except:
        return jsonify({"success": False, "message": "sql error"}), 201


if __name__ == "__main__":
    app.run(debug=True, port=8000)
