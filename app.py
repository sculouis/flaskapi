from flask import Flask
from flask import jsonify
from dataclass.Product import Product

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def get_products():
    product = Product("護手霜A1款","https://cdn.bella.tw/files/AF24A07BEE-SP-7874082.jpg","Title1",10)
    return jsonify(product)
