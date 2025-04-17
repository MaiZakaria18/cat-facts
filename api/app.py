from flask import Flask, jsonify, render_template
import random
from cat_facts import cat_facts

# Create a Flask application instance
app = Flask(__name__)

# Reusable function to get a random cat fact
def get_random_cat_fact():
    return random.choice(cat_facts)

# API endpoint: /facts
# Returns a random cat fact as a JSON response
# Example: { "fact": "Cats sleep 70% of their lives." }
@app.route('/facts')
def facts():
    return jsonify({"fact": get_random_cat_fact()})

# Web endpoint: /home
# Renders an HTML template and injects a random cat fact
# Template: templates/home.html
@app.route('/home')
def home():
    return render_template("home.html", fact=get_random_cat_fact())

# Start the Flask development server
if __name__ == '__main__':
    print("🚀 Flask app is starting...")
    app.run(debug=True)
