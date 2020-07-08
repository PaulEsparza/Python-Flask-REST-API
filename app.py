from flask import Flask, jsonify, request #pip install flask
from flask_cors import CORS #pip install flask-cors
from products import products

app = Flask(__name__)
CORS(app)

# Testing Route
@app.route('/', methods=['GET'])
def index():
    return jsonify({'response': 'Hello World!!!'})

# Get Data Routes
@app.route('/products')
def getProducts():
    return jsonify(products)

# Get Only Data Route
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify(productsFound[0])
    return jsonify({'response': 'ERROR'})

# Create Data Routes
@app.route('/products', methods=['POST'])
def createProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'response' : 'OK'})

# Update Data Route
@app.route('/products/<string:product_name>', methods=['PUT'])
def updateProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        jsonify({'response' : 'OK'})
    return jsonify({'message': 'ERROR'})

# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        jsonify({'response' : 'OK'})
    return jsonify({'message': 'ERROR'})

if __name__ == '__main__':
    app.secret_key = 'clavesecreta'
    app.run(port = 5000, debug=True)