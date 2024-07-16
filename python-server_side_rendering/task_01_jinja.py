#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Rendre un modèle HTML avec quelques données
    user_name = "Alice"
    return render_template('index.html', name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
