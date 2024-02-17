import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assuming each title is within an <a> tag that is a child of the <span> with the class 'item-title bold'
        titles = soup.find_all('span', class_=lambda x: x and 'item-title' in x and 'bold' in x)
        
        news_items = []
        for title in titles:
            # Assuming the <a> tag is a direct parent of the <span> tag
            link = title.parent['href'] if title.parent.name == 'a' else None
            news_items.append({'title': title.text.strip(), 'link': link})
        
        return news_items
    else:
        print("Failed to retrieve the webpage")
        return []

def generate_html(news_items):
    html_content = '<html><head><title>Game News</title></head><body><h1>Latest Video Game News</h1><ul>'
    
    for item in news_items:
        link = item['link'] if item['link'] else '#'
        html_content += f'<li><a href="{link}">{item["title"]}</a></li>'
    
    html_content += '</ul></body></html>'
    
    with open('game_news.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print("HTML file generated successfully.")

# Example usage
url = 'https://www.ign.com/news'  # Adjust this URL as needed
news_items = fetch_news(url)
if news_items:
    generate_html(news_items)
else:
    print("No news titles found. Check the selectors and website structure.")
