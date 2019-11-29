import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_2" \
      "?keywords=sony+a7&qid=1575020791&sr=8-2 "

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/78.0.3904.108 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if converted_price < 1.700:
        send_mail()

    print(converted_price)
    print(title.strip())

    if converted_price > 1.700:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ghouseshaik678@gmail.com', 'yetknjrgtpnknhmf')
    subject = 'Price fell down'
    body = "Check the amazon link:https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp" \
           "/B07DPSQRFF/ref=sr_1_3?keywords=sony+a7&qid=1575007644&sr=8-3 "

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'ghouseshaik678@gmail.com',
        'areebshaik528@gmail.com',
        msg
    )

    print("Email has been sent!")

    server.quit()


check_price()
