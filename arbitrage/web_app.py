from flask import Flask, render_template
from arbitrage import find_max_arbitrage_opportunity 
import requests

app = Flask(__name__)



@app.route('/')
def index():
    opportunities = find_max_arbitrage_opportunity()  
    return render_template('index.html', opportunities=opportunities)  

if __name__ == '__main__':
    app.run(debug=True)
