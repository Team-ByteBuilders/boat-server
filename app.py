from flask import Flask, request, jsonify
from connecton import *
from jwt_token import *
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/checkuser', methods = ["POST"])
def check_user():
    try:
        phone = request.json['phone']
    except:
        return jsonify({"success": False, "message": "Invalid fields"}), 201
    
    user = getUser(phone)
    if user:
        return jsonify({"success": True, "message": "User Already Exists", "data" : True}), 200
    else:
        return jsonify({"success": True, "message": "User does not exists", "data" : False}), 200

@app.route('/login', methods = ["POST"])
def loginUser():
    try:
        phone = request.json['phone']
        otp = request.json['otp']
    except:
        return jsonify({"success": False, "message": "Invalid fields"}), 201
    
    # print(phone)
    # print(otp)
    user = getUser(phone)
    if not user:
        return jsonify({"success": False, "message": "User does not exists"}), 201
    
    if(otp != '1234'):
        return jsonify({"success": False, "message": "Wrong OTP"}), 201
    id = user['id']
    print(user)
    print(id)
    token = createToken(id)

    return jsonify({"success": True, "message" : "Data received", "token" : token, "data" : user}), 200


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

# @app.route('/getallmonuments', methods = ["POST"])
# def get_monuments():


if __name__ == "__main__":
    app.run(debug=True, port=8000)
