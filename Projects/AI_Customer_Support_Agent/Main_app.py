# main.py
import streamlit as st
import os
from dotenv import load_dotenv
from sentiment_analysis import get_sentiment
from Agent_Handler import agent_handler

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Streamlit UI Config
st.set_page_config(page_title="AI Customer Support Agent", layout="wide")

# Title and Description
st.title("🤖 AI Customer Support Agent with Sentiment Analysis")
st.write(
    "Ask any question related to our product or services. The AI will assist you and analyze your sentiment."
)

# Sidebar for Model Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    model_option = st.selectbox(
        "Choose a Model", ["gemini-pro", "gemini-1.5-flash"]
    )
    temperature = st.slider(
        "Response Creativity (Temperature)", 0.0, 1.0, 0.7, step=0.1
    )

# User Query Input
user_query = st.text_input("💬 Enter your query:", "")

# Function to Get AI Response
def get_response(query, model_name, temp=0.7):
    """Get AI response through agent or Gemini API."""
    try:
        response = agent_handler(query)
        return response
    except Exception as e:
        return f"❗ Error: {str(e)}"

# Process Button
if st.button("🚀 Get Response"):
    if user_query:
        # Get AI response through agent
        with st.spinner("🤖 Generating response..."):
            response = get_response(user_query, model_option, temperature)

        # Get Sentiment
        sentiment_result = get_sentiment(user_query)

        # Display Response
        st.subheader("🤖 AI Response:")
        st.write(response)

        # Display Sentiment
        st.subheader("🧠 Sentiment Analysis:")
        st.write(f"The sentiment of your query: {sentiment_result}")

        # Optional Feedback
        feedback = st.text_area("📢 Provide feedback (optional):")
        if st.button("Submit Feedback"):
            st.success("✅ Thank you for your feedback!")
    else:
        st.warning("⚠️ Please enter a query to get a response.")
