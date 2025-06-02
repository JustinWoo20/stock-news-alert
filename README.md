# 📈  Stock News Alert

This Python script currently tracks Tesla's stock price and sends you relevant news if there’s a major movement. 
It's built with `requests` and uses the Alpha Vantage and NewsAPI APIs. While it currently tracks Tesla stock,
you can easily track another stock by changing the "stock" variable in the main.py file.

## 🔧 Features

- Checks Tesla (TSLA) daily open/close prices using Alpha Vantage
- Compares current prices to detect major swings:
  - ≥ 3% intraday movement **or**
  - ≥ 7.5% change vs. previous day close
- If either is true, the app fetches recent Tesla-related news via NewsAPI
- (Optional) Sends SMS alerts via Vonage (coming soon)

## File Structure/
stock-news-alert

    main.py # Main script to run the alert logic
    .env # Stores API keys (not committed)
    .gitignore # Ignores .env and other sensitive files
    requirements.txt # List of dependencies
    README.md # Current File
    .env.example # Example file showing the API keys currently necessary

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/stock-news-alert.git
cd stock-news-alert 
```

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Add your API keys to an .env file
Currently:
  ALPHAVANTAGE_API_KEY=your_alpha_vantage_key
  NEWS_API_KEY=your_newsapi_key

## 🧪 Running the script
python main.py # If a major stock movement is detected, it will present recent news headlines.

## 📬 Coming Soon
SMS notifications via Vonage

Email alerts

Scheduled runs with cron or Task Scheduler

Support for more stocks

## 🤝 Contributions
PRs are welcome! If you'd like to add support for a different stock or notification method, feel free to fork and open a pull request.

## 📝 License
This project is open-source and free to use under the MIT License.

## 🙋‍♂️ Contact
Feel free to reach out with feedback or suggestions

Justin

[https://github.com/JustinWoo20]