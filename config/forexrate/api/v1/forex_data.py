import yfinance as yf   

ticker = "EURUSD=X"
ticker2 = "USDJPY=X"
ticker3 = "GBPUSD=x"
ticker4 = "USDCNY=x"
ticker5 = "USDCAD=x"

start_date = "2014-01-01"
end_date = "2024-12-31"

data = yf.download(ticker, start=start_date, end=end_date)
data2 = yf.download(ticker2, start=start_date, end=end_date)
data3 = yf.download(ticker3, start=start_date, end=end_date)
data4 = yf.download(ticker4, start=start_date, end=end_date)
data5 = yf.download(ticker5, start=start_date, end=end_date)
data.to_csv("config/forexrate/forex data/eur_usd_10_years.csv")
data2.to_csv("config/forexrate/forex data/usd_jpy_10_years.csv")
data3.to_csv("config/forexrate/forex data/gbp_usd_10_years.csv")
data4.to_csv("config/forexrate/forex data/usd_cny_10_years.csv")
data5.to_csv("config/forexrate/forex data/usd_cad_10_years.csv")

