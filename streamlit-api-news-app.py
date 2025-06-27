import streamlit as st
import requests

# ---- PAGE CONFIG ----
st.set_page_config(page_title="My News App", layout="centered")

# ---- FETCH NEWS ----
API_KEY = "d01e39a93fc54e09bf91a9df57bb293a"
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
data = requests.get(URL).json()
articles = data["articles"]

# ---- SESSION STATE ----
if "index" not in st.session_state:
    st.session_state.index = 0

# ---- SAFETY CHECK ----
if not articles:
    st.error("⚠️ No articles found. Try changing the country or using a different NewsAPI endpoint.")
else:
    article = articles[st.session_state.index]

    # ---- DISPLAY NEWS CARD ----
    st.title("📰 My News App")
    image_url = article.get("urlToImage")
    fallback = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"

    try:
        st.image(image_url or fallback, width=600)
    except:
        st.image(fallback, width=600)
    st.subheader(article.get("title", "No title available"))
    st.write(article.get("description", "No description available"))

    # ---- READ MORE LINK ----
    st.markdown(f"[Read Full Article]({article['url']})", unsafe_allow_html=True)

    # ---- NAVIGATION ----
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Prev") and st.session_state.index > 0:
            st.session_state.index -= 1
    with col3:
        if st.button("Next ➡️") and st.session_state.index < len(articles) - 1:
            st.session_state.index += 1
