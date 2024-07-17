#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return str(e)

def read_csv(file_path):
    products = []
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return "Welcome to the Products API. Use /products?source=json or /products?source=csv to view products."

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error_message = None

    if source == 'json':
        result = read_json('products.json')
        if isinstance(result, str):
            error_message = f"Error reading JSON file: {result}"
        else:
            products = result
    elif source == 'csv':
        result = read_csv('products.csv')
        if isinstance(result, str):
            error_message = f"Error reading CSV file: {result}"
        else:
            products = result
    else:
        error_message = "Wrong source"

    if not error_message and product_id is not None:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            error_message = "Product not found"

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)





