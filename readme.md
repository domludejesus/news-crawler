# News Aggregator

Welcome to the News Aggregator, the ultimate solution for staying updated with the latest in video gaming and OpenAI. Our platform leverages the power of web crawling to bring you the most recent updates in these domains. Designed for gaming enthusiasts and OpenAI followers alike, our aggregator ensures you're always in the loop.

## Features

- **Latest News**: Stay ahead with real-time updates from the video game industry and OpenAI developments. Our advanced web crawlers scour the web to bring you the latest articles, announcements, and updates.
- **User Profiles**: Sign up effortlessly to create your personalized profile. Log in to manage your favorite news, tailor your news feed, and keep up with the topics you care about.
- **Ease of Use**: Navigate through the news effortlessly with our user-friendly interface. Get access to the information you want with just a few clicks.
- **SQLite Database**: Securely store your preferences and profile details in an SQLite database for fast and reliable access.

## Getting Started

Follow these steps to get your News Aggregator up and running:

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/news-aggregator.git
    ```

2. **Set up a virtual environment**

    Navigate to the project directory and set up a virtual environment:

    ```bash
    cd news-aggregator
    python -m venv venv
    ```

3. **Activate the virtual environment**

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source venv/bin/activate
    ```

4. **Install dependencies**

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask application**

    Set the environment variable and start the Flask app:

    ```bash
    export FLASK_APP=app.py # Use 'set' instead of 'export' on Windows
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000/`.

## Technology Stack

- **Backend**: Python Flask for the backend, handling web crawling, database management, and server-side logic.
- **Frontend**: Simple and responsive UI designed with HTML and CSS.
- **Database**: SQLite for storing user profiles and preferences.
- **Web Crawling**: Python scripts utilizing libraries such as Beautiful Soup for efficient data extraction.

## Upcoming Features

- **Enhanced Personalization**: More customization options for your news feed, allowing you to follow specific topics or sources closely.
- **Social Sharing**: Ability to share news directly on social media platforms from the aggregator.
- **Mobile Optimization**: Improving the mobile user experience to keep you informed on the go.

## Contributing

Interested in contributing to the News Aggregator? We welcome contributions from the community. Please check out our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Got questions or feedback? Reach out to us at [your_email@example.com](mailto:your_email@example.com).

Explore the world of video games and OpenAI with the News Aggregator – your source for the latest news.
