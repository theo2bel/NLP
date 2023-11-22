import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

# Streamlit app
def main():
    st.title("Sentiment Analysis App")

    # User input for text
    user_input = st.text_area("Enter text for sentiment analysis:", "")

    if st.button("Analyze Sentiment"):
        if user_input:
            # Perform sentiment analysis
            result = sentiment_pipeline(user_input)

            # Display the result
            st.write("Sentiment Analysis Result:")
            st.write(f"Text: {user_input}")
            st.write(f"Sentiment: {result[0]['label']}")
            st.write(f"Confidence: {result[0]['score']:.4f}")
        else:
            st.warning("Please enter text for sentiment analysis.")

if __name__ == "__main__":
    main()
