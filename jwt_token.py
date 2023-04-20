import jwt
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from functools import wraps

secret = "thisisasecret"


def token_required(f):
    @wraps(f)
    def decorated():
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({"success": False, "message": "Auth Token missing"}), 201

        print(token)
        return jsonify({"success": True, "message": "Auth Token received"}), 200

    return decorated


def createToken(id):
    jwtToken = jwt.encode({
        'phone': id,
        'exp': datetime.utcnow()
    }, secret)

    return jwtToken
