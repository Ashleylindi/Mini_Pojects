import requests
from bs4 import BeautifulSoup

# Function to scrape quotes from a website
def scrape_quotes():
    url = 'http://quotes.toscrape.com/'
    response = requests.get(url)

    if response.status_code == 200:  # If the request is successful
        soup = BeautifulSoup(response.text, 'html.parser')  # Parsing the HTML content
        quotes = soup.find_all('span', class_='text')

        for quote in quotes:
            print(quote.get_text())  # Printing each quote
    else:
        print('Failed to retrieve the webpage')

scrape_quotes()