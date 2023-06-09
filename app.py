from flask import Flask, request, jsonify
from connecton import *
from jwt_token import *
from flask_cors import CORS
import json
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import secure_filename

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/checkuser', methods=["POST"])
def check_user():
    try:
        phone = request.json['phone']
    except:
        return jsonify({"success": False, "message": "Invalid fields"}), 201

    user = getUser(phone)
    if user:
        return jsonify({"success": True, "message": "User Already Exists", "data": True}), 200
    else:
        return jsonify({"success": True, "message": "User does not exists", "data": False}), 200


@app.route('/login', methods=["POST"])
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

    if (otp != '1234'):
        return jsonify({"success": False, "message": "Wrong OTP"}), 201
    id = user['id']
    token = createToken(phone)

    return jsonify({"success": True, "message": "Login Successful", "token": token, "data": user}), 200


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


@app.route('/signup', methods=["POST"])
def signup():
    data = dict(request.form)
    try:
        name = data.get('name')
        age = data.get('age')
        phone = data.get('phone')
        face = request.files['file']
    except:
        return jsonify({"success": False, "message": "Invalid fields"}), 201
    try:
        face.save(secure_filename(face.filename))
    except:
        pass
    user = {
        name: name,
        age: age,
        phone: phone
    }

    addUser(name, age, phone)
    token = createToken(phone)

    return jsonify({"success": True, "message": "Signup successful", "token": token, "data": {name: name, age: age, phone: phone}}), 200


@app.route('/getallmonuments', methods=["POST"])
def get_monuments():
    # try:
    #     lat = request.json['lat']
    #     long = request.json['long']
    # except:
    #     return jsonify({"success": False, "message": "Invalid fields"}), 201
    list = getMonuments()
    print(list)
    return jsonify({"success": True, "message": "Data retrieved successfully", "data": list}), 200


@app.route('/getmoney', methods=["GET"])
@token_required
def get_money(user):
    return jsonify({"success": True, "message": "Balance retrieved successfully", "data": {"balance": user['money']}}), 200


@app.route('/addmoney', methods=['PUT'])
@token_required
def add_money(user):
    try:
        amt = request.json['amount']
    except:
        return jsonify({"success": False, "message": "Invalid fields"}), 201
    phone = user['phone']
    updatedBalance = user['money'] + amt
    try:
        addMoney(updatedBalance, phone)
    except:
        return jsonify({"success": False, "message": "Sql error"}), 201

    return jsonify({"success": True, "message": "Balance updated successfully", "data": {"balance": updatedBalance}}), 200

    return jsonify({"success": True, "message": "Data retrieved successfully", "data": list}), 200


@app.route('/checkout', methods=['POST'])
def checkout():
    data = dict(request.form)
    try:
        name = data.get('name')
        print(name)
        image = request.files['file']
        print(image.filename)
    except:
        return jsonify({"success": False, "message": "Invalid fields"}), 201
    try:
        image.save(name + ".jpg")
    except:
        pass
    return jsonify({"success": True, "message": " successful", }), 200


if __name__ == "__main__":
    app.run(debug=True, port=8000)
