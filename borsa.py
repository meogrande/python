# !pip install pandas requests BeautifulSoup4 
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time 
from datetime import date, timedelta
today = date.today()
base_url = "https://www.borsaitaliana.it/borsa/obbligazioni/mot/euro-obbligazioni/lista.html"
all_pages_reviews =[]

def sort_stock(stock):
    return stock.index

class Bot:
    isin = ""
    name = ""
    value = 100
    expiry_date = date.today
    ratio = 0
    def __str__(self):
        return self.isin + " " + self.name + " " + str(self.expiry_date) + " " + str(self.ratio) + " "+ str(self.value) + " ytd:" + str(self.index)
    def computeIndex(self):
        return -(self.value-100-(self.ratio*((self.expiry_date-today).days/365)))/((self.expiry_date-today).days/365)
        #return (self.expiry_date)
        #return timedelta(days = self.expiry_date-today)
        #return (self.expiry_date-today).days/365
    
def scraper():
    for i in range(1,59): # fetching reviews from five pages
        pagewise_bots = [] 
        query_parameter = "?page="+str(i)
        url = base_url + query_parameter
        response = requests.get(url)
        # print(url)
        #soup = bs(response.content, 'html.parser')
        soup = bs(response.content, 'html5lib')
        # print (soup)
        bot_tr = soup.findAll("tr")
        #rev_div = soup.find_all("a",attrs={"class","t-text"})
        print("Trovati %d elementi" % len(bot_tr))
        #print(rev_div);
        
        # Scorro tutte le righe tr della pagina
        for j in range(len(bot_tr)):
        # Per ogni tr devo prendere i vari campi
            # print(bot_tr[j].findAll('span',attrs={"class","t-text"}))
            spans_data = bot_tr[j].findAll('span',attrs={"class","t-text"})
            if len(spans_data)>0 :
                b = Bot()
                # print(spans_data[8].text.strip());
                b.isin = spans_data[0].text.strip()
                b.name = spans_data[6].text.strip()
                b.data = spans_data[9].text.strip()
                year = int(b.data[6:10])
                month = int(b.data[3:5])
                day = int(b.data[0:2])
                b.expiry_date = date(year, month, day)
                # print(spans_data[10].text.strip())
                value = spans_data[10].text.strip().replace(",",".",1)
                if value!="": # Inserisco il valore se non è vuoto
                    b.value=float(value)
                ratio = spans_data[8].text.strip().replace(",",".",1)
                if ratio!="": # Inserisco la percentuale se non è vuota
                    b.ratio = float(ratio) 
                # calcolo l'indice
                b.index = b.computeIndex();
                # print("Trovati %d span" % len(pagewise_reviews))
                pagewise_bots.append(b)
                
        # metto tutti i dati in un array
        for k in range(len(pagewise_bots)):
            all_pages_reviews.append(pagewise_bots[k])

    print(len(all_pages_reviews))
    return all_pages_reviews

# Driver code
reviews = scraper()
reviews.sort( key=sort_stock, reverse=True)
for i in range(len(reviews)):
    if reviews[i].index>1:
        print(reviews[i])
i = range(1, len(reviews)+1)
reviews_df = pd.DataFrame({'review':reviews}, index=i)
reviews_df.to_csv('bot.txt', sep='t')
