from alpaca_trade_api.rest import REST, TimeFrame
import sys

BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = sys.argv[1]
ALPACA_SECRET_KEY = sys.argv[2]

api = REST(ALPACA_API_KEY,ALPACA_SECRET_KEY,BASE_URL)

account = api.get_account()

print("Your account is:" + account.status)

rawData = api.get_bars("KO", TimeFrame.Day, "2021-06-01", "2021-07-07", limit=10, adjustment='raw').df

print(rawData)

order = api.submit_order(
    symbol='KO',
    qty=1,
    side='buy',
    type='market',
    time_in_force='day',
)

print(order)