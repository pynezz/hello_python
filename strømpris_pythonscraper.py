#   Et skript som henter dagens strømpris
import requests
from bs4 import BeautifulSoup
from datetime import date

def find_price():
    URL = 'https://www.skandiaenergi.no/dagens-strompriser/'    # Dette er nettstedet strømprisen hentes fra
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189'}

    page = requests.get(URL, headers=headers)                   # Finne nettsiden med requests lib
    soup = BeautifulSoup(page.content, 'html.parser')           # Bruke bs4, gi bs4 nettsiden og bruke html parser

    found_price = soup.find(id="no1").find('p').get_text()      # Finne div id til strømprisen, finne <p> taggen med prisen og hente teksten
    print (f"{date.today().strftime('%d.%B %Y')}: {found_price} øre/kWh")

find_price()                                                    # Kjører funkjsonen find_price()