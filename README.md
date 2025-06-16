# 📰 Streamlit API News App

A real-time news reader dashboard built with Streamlit and powered by NewsAPI. Browse top headlines interactively using dynamic navigation buttons and clean visuals.

## 💡 Features
- Fetches real-time top headlines from NewsAPI
- Built with Streamlit for a smooth, browser-based experience
- Displays image, title, description, and external link for each article
- "Previous" and "Next" buttons for article navigation
- Error handling for empty responses and image issues

## 🛠 Tech Stack
- Python 3.x
- Streamlit
- Requests

## 📦 Installation
```bash
pip install streamlit requests
🚀 How to Run the App
bash
Copy
Edit
streamlit run streamlit-api-news-app.py
🔐 Note on API Key
This app uses a free NewsAPI key. You can get your own from newsapi.org.
Replace the API key in this line:

python
Copy
Edit
API_KEY = "your_own_api_key"
🔄 Optional: Change Country or Query
You can modify the URL to change the country or use a keyword query:

python
Copy
Edit
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
✅ Outcome
A polished Python project that showcases how to connect APIs, manage session state, and handle real-world errors — perfect for data app prototyping and dashboards.
