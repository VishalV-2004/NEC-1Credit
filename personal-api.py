from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])  # Added a default route
def home():
    return jsonify({"message": "Welcome to Vishal's API!"})

@app.route('/name', methods=['GET'])
def get_name():
    return jsonify({"name": "Vishal"})

@app.route('/register_number', methods=['GET'])
def get_register_number():
    return jsonify({"register_number": "22it055"})

@app.route('/department', methods=['GET'])
def get_department():
    return jsonify({"department": "Information Technology"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
