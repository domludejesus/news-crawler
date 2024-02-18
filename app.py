from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, login_manager
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def fetch_news(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    news_items = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('a', href=True)
        for article in articles:
            title_span = article.find('span', class_=lambda x: x and 'item-title' in x and 'bold' in x)
            if title_span:
                title = title_span.text.strip()
                link = article['href']
                if not link.startswith('http'):
                    link = urljoin(url, link)
                news_items.append({'title': title, 'link': link})
    return news_items

@app.route('/')
def home():
    return render_template('index.html', is_authenticated=current_user.is_authenticated)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']  # Assuming you've added an email field in your form
        password = generate_password_hash(request.form['password'])
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/fetch-news')
@login_required
def get_news():
    url = 'https://www.ign.com/news'
    news_items = fetch_news(url)
    return {'titles': news_items}

@app.route('/fetch-ai-news')
@login_required
def fetch_ai_news():
    url = 'https://openai.com/blog'
    news_items = []
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Assuming the h3 tag is wrapped in or followed by an <a> tag
        articles = soup.find_all('h3', class_='f-subhead-2 mt-8')
        for article in articles:
            title = article.text.strip()
            # Navigate to the parent or next sibling <a> tag to get the link
            link = article.find_parent('a')['href'] if article.find_parent('a') else None
            if link and not link.startswith('http'):
                link = urljoin(url, link)
            if link:  # Ensure there's a link before adding to the list
                news_items.append({'title': title, 'link': link})
    return {'titles': news_items}



if __name__ == '__main__':
    app.run(debug=True)
