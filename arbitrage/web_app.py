from flask import Flask, render_template
from arbitrage import find_max_arbitrage_opportunity  # Import the arbitrage script function
import requests

app = Flask(__name__)

# ... Other Flask app configurations ...

@app.route('/')
def index():
    opportunities = find_max_arbitrage_opportunity()  # Call the arbitrage script to fetch opportunities
    return render_template('index.html', opportunities=opportunities)  # Render the HTML template with opportunities

if __name__ == '__main__':
    app.run(debug=True)
