from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Order Database (Isolated)
orders = []

# URLs to other microservices (using container names for DNS resolution!)
USER_SERVICE_URL = "http://192.168.81.151:5001"
PRODUCT_SERVICE_URL = "http://192.168.81.151:5002"

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'user_id' not in data or 'product_id' not in data:
        return jsonify({"error": "Missing user_id or product_id"}), 400

    user_id = data['user_id']
    product_id = data['product_id']

    # 1. Talk to User Service via HTTP
    try:
        user_resp = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
        if user_resp.status_code != 200:
            return jsonify({"error": "User validation failed"}), 400
        user_data = user_resp.json()
    except requests.exceptions.RequestException:
        return jsonify({"error": "User Service is down!"}), 500

    # 2. Talk to Product Service via HTTP
    try:
        prod_resp = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
        if prod_resp.status_code != 200:
            return jsonify({"error": "Product validation failed"}), 400
        product_data = prod_resp.json()
    except requests.exceptions.RequestException:
        return jsonify({"error": "Product Service is down!"}), 500

    if product_data["stock"] <= 0:
        return jsonify({"error": "Product out of stock"}), 400

    # 3. Reduce stock in Product Service
    try:
        stock_resp = requests.put(f"{PRODUCT_SERVICE_URL}/products/{product_id}/reduce_stock")
        if stock_resp.status_code != 200:
             return jsonify({"error": "Failed to update stock"}), 500
    except requests.exceptions.RequestException:
        return jsonify({"error": "Product Service is down!"}), 500

    # 4. Save the order
    order = {
        "id": len(orders) + 1,
        "user_name": user_data["name"],
        "product_name": product_data["name"],
        "total_price": product_data["price"]
    }
    orders.append(order)

    return jsonify({"message": "Order created successfully", "order": order}), 201

if __name__ == '__main__':
    print("Starting Order Service on Port 5003")
    app.run(debug=True, host='0.0.0.0', port=5003)