from bs4 import BeautifulSoup
import requests

StockID = "2330" 

def crawl_stock_news(StockID):
  url = 'https://tw.stock.yahoo.com/quote/'+StockID+'/news'
  r = requests.get(url)
  soup = BeautifulSoup(r.text,'html.parser')
  for l in soup.find_all(class_="js-stream-content Pos(r)"):
    news = l.text
    if '廣告' not in news:
        print(f"\033[34;1m{news}\033[0m",'\n')

crawl_stock_news(StockID)