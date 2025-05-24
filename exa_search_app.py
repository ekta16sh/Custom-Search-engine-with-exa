import streamlit as st
import requests

# 1. CONFIGURATION
EXA_API_KEY = "a6303a26-a216-462b-af77-3a55e4740b74"  # 🔁 Replace this with your actual API key
SEARCH_ENDPOINT = "https://api.exa.ai/search"

# 2. STREAMLIT UI
st.set_page_config(page_title="Exa Search", layout="centered")
st.title("🔍 Custom Search Engine with Exa")

query = st.text_input("Enter your search query:", placeholder="e.g. latest advancements in robotics")

# Optional: number of results
num_results = st.slider("Number of results:", 1, 10, 5)

if st.button("Search") and query:
    with st.spinner("Searching Exa.ai..."):
        try:
            # 3. CALL EXA API
            response = requests.post(
                SEARCH_ENDPOINT,
                headers={
                    "Authorization": f"Bearer {EXA_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "query": query,
                    "numResults": num_results
                }
            )

            data = response.json()

            # 4. DISPLAY RESULTS
            if "results" in data:
                st.success(f"Showing top {len(data['results'])} results for: **{query}**")
                for result in data["results"]:
                    st.subheader(result.get("title", "Untitled"))
                    st.write(result.get("text", ""))
                    st.markdown(f"[🔗 View Source]({result.get('url')})", unsafe_allow_html=True)
                    st.markdown("---")
            else:
                st.warning("No results found or invalid API response.")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
