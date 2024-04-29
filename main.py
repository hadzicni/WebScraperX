import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        article_headlines = soup.find_all('h2', class_='headline')
        for headline in article_headlines:
            print(headline.text.strip())
        
        weather_forecast = soup.find('div', class_='weather-forecast')
        print(weather_forecast.text.strip())
        
        stock_prices = soup.find_all('span', class_='stock-price')
        for price in stock_prices:
            print(price.text.strip())
        
        product_reviews = soup.find_all('div', class_='product-review')
        for review in product_reviews:
            print(review.text.strip())
        
    else:
        print("Fehler beim Abrufen der Webseite.")

url = 'https://example.com/news'
scrape_website(url)
