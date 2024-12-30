import yfinance as yf   

ticker = "EURUSD=X"

start_date = "2014-01-01"
end_date = "2024-01-01"

data = yf.download(ticker, start=start_date, end=end_date)


data.to_csv("config/forexrate/forex data/eur_usd_10_years.csv")

print(data.head())