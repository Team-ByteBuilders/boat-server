import jwt
from flask import Flask, request, jsonify
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated():
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({"success" : False, "message" : "Auth Token missing"}), 201
        
        print(token)
        return jsonify({"success" : True, "message" : "Auth Token received"}), 200

    return decorated