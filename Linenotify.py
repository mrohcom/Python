from requests_html import HTMLSession
from bs4 import BeautifulSoup
from line_notify import LineNotify
import schedule
import time

def sendNotfiy():
    ACCESS_TOKEN = "hZI3bXOrDac7zZ5UyqHZL2vr3vPZE4Pesi320TYpSXb"

    notify = LineNotify(ACCESS_TOKEN)

    url_path = "https://www.mir4draco.com/price"
    session = HTMLSession()
    r = session.get(url_path)
    r.html.render(wait=8, sleep=8)
    url_path = r.html

    soup = BeautifulSoup(url_path.html, 'html.parser')
    price_raw = soup.find_all(class_ = "amount")
    price = []

    for i in price_raw :
        price.append(i.text)

    url_wemix = "https://coinmarketcap.com/th/currencies/wemix/"
    session = HTMLSession()
    r = session.get(url_wemix)
    r.html.render(wait=8, sleep=8)
    url_wemix = r.html

    soup_wemix = BeautifulSoup(url_wemix.html, 'html.parser')
    price_wemix_raw = soup_wemix.find_all(class_="priceValue")
    price_wemix = []

    for i in price_wemix_raw:
        price_wemix.append(i.text)

    url_thb = "https://coinmarketcap.com/th/currencies/tether/"
    session = HTMLSession()
    r = session.get(url_thb)
    r.html.render(wait=8, sleep=8)
    url_thb = r.html

    soup = BeautifulSoup(url_thb.html, 'html.parser')
    price_raw = soup.find_all(class_="priceValue")
    price_thb = []

    for i in price_raw:
        price_thb.append(i.text)



    pricedarco = price[1]
    pricedarco = float(pricedarco[1:7])

    thb_usd = price_thb[0]
    thb_usd = float(thb_usd[1:5])

    pricedarco = thb_usd*pricedarco

    pricedarco = "%.2f" % round(pricedarco, 2)

    lineNotify = "\nWEMIX-THB : "+price_wemix[0]+"\nDRACO-THB : ฿"+str(pricedarco)+"\nWEMIX-DRACO : ₵"+price[0]+"\nDARCO-DARKSTEEL : "+price[2]

    notify.send(lineNotify)


schedule.every(1).minutes.do(sendNotfiy)

while True:
    schedule.run_pending()
    time.sleep(1)