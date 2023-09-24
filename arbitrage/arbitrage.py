import requests


def get_binance_latest_trade_price():
    url = 'https://api.binance.com/api/v3/ticker/price'
    symbol = 'BTCUSDT'
    params = {'symbol': symbol}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        ticker_data = response.json()
        latest_trade_price = float(ticker_data['price'])
        return latest_trade_price
    else:
        print('Failed to retrieve ticker price from Binance. Status code:', response.status_code)
        return None


def get_coinbase_pro_last_trade_price():
    url = 'https://api.pro.coinbase.com/products/BTC-USD/ticker'

    response = requests.get(url)

    if response.status_code == 200:
        ticker_data = response.json()
        current_price = float(ticker_data['price'])
        return current_price
    else:
        print('Failed to retrieve ticker data from Coinbase Pro. Status code:', response.status_code)
        return None


def get_gateio_latest_trade_price():
    url = 'https://api.gate.io/api2/1/ticker/btc_usdt'

    response = requests.get(url)

    if response.status_code == 200:
        ticker_data = response.json()
        latest_trade_price = float(ticker_data['last'])
        return latest_trade_price
    else:
        print('Failed to retrieve ticker price from gate.io. Status code:', response.status_code)
        return None


def find_max_arbitrage_opportunity():
    binance_price = get_binance_latest_trade_price()
    coinbase_price = get_coinbase_pro_last_trade_price()
    gateio_price = get_gateio_latest_trade_price()

    opportunities = []  # 

    if binance_price is not None and coinbase_price is not None and gateio_price is not None:
        price_difference_bc = binance_price - coinbase_price
        price_difference_bg = binance_price - gateio_price
        price_difference_cg = coinbase_price - gateio_price

        max_difference = max(price_difference_bc, price_difference_bg, price_difference_cg)

        if max_difference == price_difference_bc:
            profit_percent = (abs(price_difference_bc) / coinbase_price) * 100
            opportunities.append(f'Buy on Coinbase Pro, Sell on Binance. Profit: {abs(price_difference_bc):.2f} USD ({profit_percent:.2f}%)')
        elif max_difference == price_difference_bg:
            profit_percent = (abs(price_difference_bg) / gateio_price) * 100
            opportunities.append(f'Buy on gate.io, Sell on Binance. Profit: {abs(price_difference_bg):.2f} USD ({profit_percent:.2f}%)')
        else:
            profit_percent = (abs(price_difference_cg) / gateio_price) * 100
            opportunities.append(f'Buy on gate.io, Sell on Coinbase Pro. Profit: {abs(price_difference_cg):.2f} USD ({profit_percent:.2f}%)')
    else:
        opportunities.append('Price comparison failed due to missing data.')

    return opportunities  


def main():
    find_max_arbitrage_opportunity()

if __name__ == '__main__':
    main()
