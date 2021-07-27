from analysis import NumAnalysis
from alpaca_trade_api.rest import REST
import sys

BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = sys.argv[1]
ALPACA_SECRET_KEY = sys.argv[2]

api = REST(ALPACA_API_KEY,ALPACA_SECRET_KEY,BASE_URL)

result = NumAnalysis(api).IsActive()
assert result == "ACTIVE"

result = NumAnalysis(api).IsBuy("TSLA")
print("Is Tesla a buy?")
print(result)

print("Is Peloton a buy?")
print(NumAnalysis(api).IsBuy("PTON"))