import os
from twilio.rest import Client
from dotenv import load_dotenv
import requests

load_dotenv()


def set_message_server():
    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    return Client(account_sid, auth_token)


def get_dates(data: dict):
    return data.keys()


def get_stock_market_information():
    stocks: dict = {}
    alpha_params = {'function': 'TIME_SERIES_DAILY',
                    'symbol': STOCK,
                    'interval': '60min',
                    'apikey': 'KZRCTTFNW9M5750V'}
    endpoint_alpha = 'https://www.alphavantage.co/query'
    # STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    stock_data = requests.get(endpoint_alpha, params=alpha_params)
    stock_data.raise_for_status()
    for date, value in stock_data.json()['Time Series (Daily)'].items():
        if len(stocks) == 2:
            break
        stocks[date] = value
    return stocks


def get_earning_percentage(stock: dict):
    opening = float(stock['1. open'])
    closing = float(stock['4. close'])
    return round((((closing - opening) * 100) / opening), 2)


def get_stock_news():
    news_stock: list = []
    endpoint_news = 'https://newsapi.org'
    type_of_search = '/v2/top-headlines'
    news_search = requests.get(f"{endpoint_news}{type_of_search}", params=news_params)
    news_search.raise_for_status()
    company_news = news_search.json()
    for ind, news_search in enumerate(company_news.get('articles')):
        if ind > 2:
            break
        news_stock.append(f"Headline: {news_search['title']}"
                          f"\nBrief: {news_search['description']}")
    return news_stock


MY_NUMBER = '+584147533905'
DELIVER_NUMBER = os.getenv('PHONE_SENDER')
STOCK = "TSLA"
COMPANY_NAME = 'Tesla'
daily_stock = get_stock_market_information()
f_period, s_period = get_dates(daily_stock)
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_params = {'q': COMPANY_NAME,
               'category': 'business',
               'language': 'en',
               'country': 'us',
               'from': s_period,
               'to': f_period,
               'apikey': os.getenv('NEWSAPI_API_KEY')
               }
tesla_news = get_stock_news()
client = set_message_server()

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
stock_liability_today = get_earning_percentage(daily_stock[f_period])
stock_liability_yesterday = get_earning_percentage(daily_stock[s_period])
trend = "\u25B2"
if 0 < stock_liability_today > stock_liability_yesterday:
    trend = "\u25BC"
for news in tesla_news:
    stock_message = f"{STOCK}:\n {trend}{abs(stock_liability_today)}%\n{news}"
    my_message = client.messages.create(
                                        from_=DELIVER_NUMBER,
                                        body=stock_message,
                                        to=MY_NUMBER
    )
    print(my_message.status)
