import jwt
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from functools import wraps
from connecton import *
secret = "thisisasecret"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({"success": False, "message": "Auth Token missing"}), 201

        print(token)
        token = str.replace(str(token), 'Bearer ', '')
        data = jwt.decode(token, secret, algorithms=['HS256'])
        print(data['phone'])
        user = getUser(data['phone'])
        return f(user, *args, **kwargs)

    return decorated


def createToken(id):
    jwtToken = jwt.encode({
        'phone': id
    }, secret)

    return jwtToken
