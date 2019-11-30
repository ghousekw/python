# Amazon product price tracking using Python 
# Get all libs
import bs4 as bs
import sys
import schedule
import time
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl


class HTMLPage(QWebEnginePage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load Done.')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


def Amazon_exact_url(url):
    index = url.find("B0")
    index = index + 10
    current_url = ""
    current_url = url[:index]
    return current_url


def Amazon_handler():
    url = "https://www.amazon.in/Oppo-Aurora-Blue-64GB-Storage/dp/B07PQ7CXLV/"
    # Get url to extract data
    exacturl = Amazon_exact_url(url)
    ProductPage = HTMLPage(exacturl)
    soup = bs.BeautifulSoup(ProductPage.html, 'html.parser')
    js_test = soup.find('span', id='priceblock_ourprice')
    if js_test is None:
        js_test = soup.find('span', id='priceblock_dealprice')
    str = ""
    for line in js_test.stripped_strings:
        str = line

    # To integer
    str = str.replace(", ", "")
    current_price = int(float(str))
    our_price = 20000
    if current_price < our_price:
        print("Price Dropped. Get the deal")
    else:
        print("Price is high. Bad Deal")


def TrackerJob():
    print("Working....")
    Amazon_handler()


# main Function
# Here I am checking price every 10 minutes, you can set your own time
schedule.every(10).minutes.do(TrackerJob)

while True:
    schedule.run_pending()
    time.sleep(60*60)
