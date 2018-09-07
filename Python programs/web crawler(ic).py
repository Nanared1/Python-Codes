## buckysroom.org/trade/index.php   search.php?page=2
#Nana Abekah
from bs4 import BeautifulSoup
import requests

def trade_spider(max_pages):
    page = 1;
    while(page < max_pages):
        url = 'https://www.ebay.ca/sch/i.html?_from=R40&_nkw=watch&_sacat=0&_pgn='+str(page);
        source_code = requests.get(url);
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text);

trade_spider(2);
