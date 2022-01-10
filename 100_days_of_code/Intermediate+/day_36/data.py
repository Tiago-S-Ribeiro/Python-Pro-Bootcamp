import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCKS_PRICES_API_KEY = os.environ.get("STOCKS_PRICES_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACC_SSID = os.environ.get("TWILIO_ACC_SSID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
CALLER = os.environ.get("CALLER")
RECEIVER = "<<RECEIVER_PHONE_NUMBER>>"