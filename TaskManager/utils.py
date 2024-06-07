import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCap:
    BASE_URL = "https://coinmarketcap.com/currencies/"

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def scrape_coin_data(self, coin):
        url = f"{self.BASE_URL}{coin.lower()}/"
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        
        # Extract data (example for DUKO)
        data = {
            'price': float(soup.find('div', class_='priceValue').text.strip('$')),
            'price_change': float(soup.find('span', class_='sc-15yy2pl-0 feeyND').text.strip('%')),
            'market_cap': int(soup.find('div', class_='statsValue').text.strip('$').replace(',', '')),
            # Continue extracting other fields...
        }

        # Extract contract, official links, socials, etc.
        # Example extraction code, needs adaptation based on actual page structure
        contracts = []
        for contract in soup.select('.sc-16r8icm-0'):
            contracts.append({
                'name': contract.text.split()[0],
                'address': contract.find('a')['href'].split('/')[-1]
            })

        data['contracts'] = contracts
        # Extract other fields similarly...
        return data
