from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Internal DNS routing to our backend microservices
# USER_SVC_URL = "http://user-service:5001"
# PRODUCT_SVC_URL = "http://product-service:5002"
# ORDER_SVC_URL = "http://order-service:5003"

USER_SVC_URL = "http://192.168.81.151:5001"
PRODUCT_SVC_URL = "http://192.168.81.151:5002"
ORDER_SVC_URL = "http://192.168.81.151:5003"



# ==========================================
# ENDPOINTS (Proxy / API Gateway)
# ==========================================
@app.route('/')
def home():
    """Serves the main UI."""
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def proxy_users():
    """Proxy request to the isolated User Service."""
    try:
        resp = requests.get(f"{USER_SVC_URL}/users", timeout=5)
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"users": [], "error": "User service unreachable"}), 503

@app.route('/api/products', methods=['GET'])
def proxy_products():
    """Proxy request to the isolated Product Service."""
    try:
        resp = requests.get(f"{PRODUCT_SVC_URL}/products", timeout=5)
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"products": [], "error": "Product service unreachable"}), 503

@app.route('/api/orders', methods=['POST'])
def proxy_orders():
    """Proxy order creation to the isolated Order Service."""
    try:
        resp = requests.post(f"{ORDER_SVC_URL}/orders", json=request.json, timeout=5)
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Order service unreachable"}), 503

if __name__ == '__main__':
    print("Starting Frontend Gateway UI on Port 5000")
    app.run(debug=True, host='0.0.0.0', port=5000)