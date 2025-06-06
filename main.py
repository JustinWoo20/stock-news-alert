import os
from dotenv import load_dotenv
from datetime import date, timedelta
import requests

load_dotenv()

today = date.today()
yesterday = date.today() - timedelta(days=1)
no_news = True
MAX_LOOKBACK_DAYS = 10
attempts = 0

# Stock and Alphavantage
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHVANTAGE_API_KEY,
}
#Newsapi
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = os.getenv("NEWS_API_KEY")
print(NEWS_API)
news_parameters = {
    "apiKey": NEWS_API,
    "q": "Tesla OR Elon OR Musk OR 'Elon Musk'",
    "pageSize": 5,
    "from": str(yesterday),
    "to": str(today),
    "language": "en",
}

# Get Stock Data
stock_response = requests.get(url=STOCK_ENDPOINT, params=alphavantage_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Get news articles
def get_articles(endpoint, endpoint_parameters):
    news_response = requests.get(url=endpoint, params=endpoint_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]

    all_breaking_news = []
    for article in articles:
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        breaking_news = f"Headline: {title}\nBrief: {description}\n URL: {url}\n"
        all_breaking_news.append(breaking_news)
    return "\n".join(all_breaking_news)


while attempts <= MAX_LOOKBACK_DAYS:
    try:
        # Get today's opening and closing prices
        today_open = float(stock_data["Time Series (Daily)"][str(today)]["1. open"])
        today_close = float(stock_data["Time Series (Daily)"][str(today)]["4. close"])
        # Get yesterday's closing
        yesterday_close = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])
        # Compare today's opening and closing prices
        if abs((today_close - today_open) / today_open) >= .030 or abs((today_close - yesterday_close) / yesterday_close) >= .075:
            news = get_articles(NEWS_ENDPOINT, news_parameters)
            print(news)
            no_news = False
        else:
            print(f"There were no major price movements for {STOCK} stock recently.")
        break
    except KeyError:
        today -= timedelta(days=1)
        yesterday -= timedelta(days=1)
        attempts += 1
else:
    print(f"There is no valid data for {STOCK} stock.")

