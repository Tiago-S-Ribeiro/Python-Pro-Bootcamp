import requests
from twilio.rest import Client
from data import STOCKS_PRICES_API_KEY, STOCK_ENDPOINT, NEWS_ENDPOINT, NEWS_API_KEY, TWILIO_ACC_SSID, TWILIO_AUTH_TOKEN, CALLER, RECEIVER, STOCK_NAME, COMPANY_NAME

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCKS_PRICES_API_KEY
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "language": "en",
    "sortBy": "popularity"
}

def calc_percentage(value_1: float, value_2: float) -> float:
    abs_diff = round(abs(value_1 - value_2), 2)
    avg = (value_1 + value_2) / 2
    perc = (abs_diff / avg) * 100
    
    return round(perc, 2)

def send_text(message: str):
    client = Client(TWILIO_ACC_SSID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(body=message, from_=CALLER, to=RECEIVER)
    
    print(message.status)

#Stocks
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stocks_movements = [value for (key,value) in stock_response.json()["Time Series (Daily)"].items()]

#Get last 2 days market closing price for the stock
yesterday_closing_price = round(float(stocks_movements[0]["4. close"]), 2)
ereyesterday_closing_price = round(float(stocks_movements[1]["4. close"]), 2)
#Calculate the difference % between both days
percentage_diff = calc_percentage(yesterday_closing_price, ereyesterday_closing_price)

#News
news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
top_3_news = news_response.json()["articles"][:3]

symbol = '🔺' if yesterday_closing_price > ereyesterday_closing_price else '🔻'

for news in top_3_news:
    message_body = f"\n{COMPANY_NAME}: {symbol}{percentage_diff}%\nHeadline: {news['title']}\nBrief: {news['description']}"
    send_text(message_body)
    