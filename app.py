from flask import Flask, request, jsonify
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
        return jsonify({"success" : False, "message" : "Invalid fields"})
    print(monument_details)
    print(monument_name)
    print(registration_fees)
    print(image_url)
    print(coor_lat)
    print(coor_long)

    return jsonify({"success" : True, "message" : "Monument added successfully"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)