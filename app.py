from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Your API key for Alpha Vantage
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

# Dummy data for favorite stocks
favorites = []

@app.route('/')
def index():
    return render_template('index.html', favorites=favorites)

@app.route('/search', methods=['POST'])
def search():
    symbol = request.form['symbol']
    data = get_stock_data(symbol)
    if data:
        return render_template('index.html', data=data, symbol=symbol, favorites=favorites)
    else:
        flash('Stock symbol not found or API limit reached.')
        return redirect(url_for('index'))

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    symbol = request.form['symbol']
    if symbol not in favorites:
        favorites.append(symbol)
    return redirect(url_for('index'))

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    symbol = request.form['symbol']
    if symbol in favorites:
        favorites.remove(symbol)
    return redirect(url_for('index'))

@app.route('/favorites')
def get_favorites():
    data = {symbol: get_stock_data(symbol) for symbol in favorites}
    return jsonify(data)

def get_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',  # Correct interval value
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'Time Series (5min)' in data:
            return data['Time Series (5min)']
    return None

if __name__ == '__main__':
    app.run(debug=True)
