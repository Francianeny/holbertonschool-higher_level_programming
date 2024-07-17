#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Route to handle /products?source=json&id=<optional_id>
@app.route('/products')
def display_products():
    source = request.args.get('source')  # Get the 'source' query parameter
    id = request.args.get('id')  # Get the 'id' query parameter if provided

    if source == 'json':
        # Read and parse JSON data from products.json
        with open('products.json', 'r', encoding='utf-8') as json_file:
            products = json.load(json_file)
    elif source == 'csv':
        # Read and parse CSV data from products.csv
        products = []
        with open('products.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                products.append(row)
    else:
        return "Invalid source parameter. Use 'json' or 'csv'."

    # Filter products by id if provided
    if id:
        filtered_products = [p for p in products if str(p.get('id')) == id]
    else:
        filtered_products = products

    return render_template('product_display.html', products=filtered_products)

if __name__ == '__main__':
    app.run(debug=True)



