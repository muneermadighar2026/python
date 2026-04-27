from flask import Flask, jsonify, request

app = Flask(__name__)

# ==============================================================================================================================
# IN-MEMORY DATABASE (Mocking a real DB)
# curl -X POST -H "Content-Type: application/json" -d '{"user_id": 1, "product_id": 102}' http://localhost:5000/orders
# ==============================================================================================================================
#users=['orange','apple','banana']
#users=[1,2,3]

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

products = [
    {"id": 101, "name": "Laptop", "price": 999.99, "stock": 10},
    {"id": 102, "name": "Mouse", "price": 25.50, "stock": 50}
]

orders = []

# ==========================================
# USER MODULE
# ==========================================
@app.route('/')
def home():
    return "Welcome to the E-Commerce Monolith API! Try /users, /products, or POST to /orders."
@app.route('/users', methods=['GET'])
def get_users():
    """Returns a list of all users."""
    return jsonify({"users": users}), 200

# ==========================================
# PRODUCT MODULE
# ==========================================
@app.route('/products', methods=['GET'])
def get_products():
    """Returns a list of all products."""
    return jsonify({"products": products}), 200
# ==========================================
# LIST ORDERS MODULE    
# ==========================================
@app.route('/list_orders', methods=['GET'])
def list_orders():
    """Returns a list of all orders."""
    return jsonify({"orders": orders}), 200

# ==========================================
# ORDER MODULE (The Bottleneck)
# ==========================================
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Creates an order. 
    Notice how tightly coupled this is: it directly accesses 
    the 'users' and 'products' memory structures. If this was a 
    microservice, it wouldn't have direct access to User/Product DBs!
    """
    data = request.get_json()
    
    if not data or 'user_id' not in data or 'product_id' not in data:
        return jsonify({"error": "Missing user_id or product_id"}), 400

    user_id = data['user_id']
    product_id = data['product_id']

    # 1. Tightly coupled direct lookup
    user = next((u for u in users if u["id"] == user_id), None)
    product = next((p for p in products if p["id"] == product_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404
    if not product:
        return jsonify({"error": "Product not found"}), 404

    if product["stock"] <= 0:
         return jsonify({"error": "Product out of stock"}), 400

    # 2. Process order and modify product stock directly
    product["stock"] -= 1
    
    order = {
        "id": len(orders) + 1, 
        "user_name": user["name"], 
        "product_name": product["name"],
        "total_price": product["price"]
    }
    orders.append(order)

    return jsonify({"message": "Order created successfully", "order": order}), 201

if __name__ == '__main__':
    # Run the monolith on port 5000
    print("Starting E-Commerce Monolith on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)