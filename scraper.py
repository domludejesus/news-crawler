import requests 
from bs4 import BeautifulSoup
import time

def fetch_news(url): 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = soup.find_all('h2', class_='article-name') #example selector 
    
    news_items = []
    for article in articles:
        title = article.text.strip()
        link = article.find('a')['href']
        news_items.append({'title': title, 'link':link })
    
    return news_items

url = 'https://www.ign.com/articles'
news_items = fetch_news(url)
for item in news_items:
    print(item['title'], item['link'])
    
    