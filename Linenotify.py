from requests_html import HTMLSession
from bs4 import BeautifulSoup
from line_notify import LineNotify
import schedule
import time

def sendNotfiy():
    ACCESS_TOKEN = "9kZ6LBtP5jWrX844vx6qRKtr6blhGSX7dvc7D8qrtk5"

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

    lineNotify = "\nWEMIX-DRACO : "+price[0]+"\nUSD-DRACO : "+price[1]+"\nDARCO-DARKSTEEL : "+price[2]

    notify.send(lineNotify)


schedule.every(10).minutes.do(sendNotfiy)

while True:
    schedule.run_pending()
    time.sleep(1)