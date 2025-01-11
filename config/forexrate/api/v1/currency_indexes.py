import yfinance as yf   

euro = "^STOXX"
jpy = "^N225"
usd = "DX-Y.NYB"
gbp = "^FTSE"
cny = "000001.SS"
cad = "^GSPTSE"

start_date = "2014-01-01"
end_date = "2024-12-20"

data = yf.download(euro, start=start_date, end=end_date)
data2 = yf.download(jpy, start=start_date, end=end_date)
data3 = yf.download(usd, start=start_date, end=end_date)
data4 = yf.download(gbp, start=start_date, end=end_date)
data5 = yf.download(cny, start=start_date, end=end_date)
data6 = yf.download(cad, start=start_date, end=end_date)
data.to_csv("C:/Users/vamsh/OneDrive/Desktop/Forex trading/Forex-Trading/config/forexrate/data/currency index/euro.csv")
data2.to_csv("C:/Users/vamsh/OneDrive/Desktop/Forex trading/Forex-Trading/config/forexrate/data/currency index/jpy.csv")
data3.to_csv("C:/Users/vamsh/OneDrive/Desktop/Forex trading/Forex-Trading/config/forexrate/data/currency index/usd.csv")
data4.to_csv("C:/Users/vamsh/OneDrive/Desktop/Forex trading/Forex-Trading/config/forexrate/data/currency index/gbp.csv")
data5.to_csv("C:/Users/vamsh/OneDrive/Desktop/Forex trading/Forex-Trading/config/forexrate/data/currency index/cny.csv")
data6.to_csv("C:/Users/vamsh/OneDrive/Desktop/Forex trading/Forex-Trading/config/forexrate/data/currency index/cad.csv")
