from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for cross-origin requests
CORS(app)

@app.route('/submit-cart', methods=['POST'])
def submit_cart():
    try:
        # Get JSON data from the request
        data = request.json
        print("Received cart:", data)  # For debugging
        
        # Example processing logic (you can customize this)
        if not data or not isinstance(data, list):
            return jsonify({"message": "Invalid cart data"}), 400
        
        # Simulate storing or processing the cart data
        # Here you might save to a database or perform calculations
        return jsonify({"message": "Cart submitted successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Error processing cart"}), 500

# Default route to check if the server is running
@app.route('/')
def home():
    return "Flask server is running!"

if __name__ == '__main__':
    app.run(debug=True)
