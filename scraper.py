import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Targeting the <span> elements by partial match on their class attribute
        titles = soup.find_all('span', class_=lambda x: x and 'item-title' in x and 'bold' in x)
        
        news_items = []
        for title in titles:
            news_items.append(title.text.strip())
        
        return news_items
    else:
        print("Failed to retrieve the webpage")
        return []

# Example usage
url = 'https://www.ign.com/news'  # Adjust this URL as needed
news_titles = fetch_news(url)
if news_titles:
    for title in news_titles:
        print(title)
else:
    print("No news titles found. Check the selectors and website structure.")
    
    
