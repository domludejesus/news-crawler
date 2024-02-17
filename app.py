from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_news(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    news_items = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('span', class_=lambda x: x and 'item-title' in x and 'bold' in x)
        for title in titles:
            news_item = title.text.strip()
            news_items.append(news_item)
    return news_items

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch-news')
def get_news():
    url = 'https://www.ign.com/news'  # Adjust this URL as needed
    news_titles = fetch_news(url)
    return {'titles': news_titles}

if __name__ == '__main__':
    app.run(debug=True)
