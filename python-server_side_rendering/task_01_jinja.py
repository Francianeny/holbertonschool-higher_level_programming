#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

# Route pour rendre la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Route pour rendre la page à propos
@app.route('/about')
def about():
    return render_template('about.html')

# Route pour rendre la page de contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route pour rendre la page des éléments
@app.route('/items')
def items():
    # Charger les données depuis items.json
    with open('items.json', 'r') as f:
        items_data = json.load(f)

    # Extraire la liste des éléments depuis les données JSON
    items_list = ['Item 1', 'Item 2', 'Item 3']

    # Rendre items.html avec la liste des éléments
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


