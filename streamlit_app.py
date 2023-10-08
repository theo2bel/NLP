import streamlit as st
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Tokenize and tag text
def tokenize_and_tag(text):
    doc = nlp(text)
    tokens = []
    for token in doc:
        if token.is_alpha:
            nature = token.pos_
            if nature.startswith("V"):
                color = "green"  # Verb
            elif nature.startswith("N"):
                color = "blue"   # Noun
            elif nature == "RB":
                color = "red"    # Adverb
            else:
                color = "black"  # Other
            tokens.append(f'<span style="color:{color}">{token.text}</span>')
        else:
            tokens.append(token.text)
    return " ".join(tokens)

# Streamlit app
st.title("Tokenization and Word Nature Display")

# Input text
input_text = st.text_area("Enter a text:")

# Tokenize and display the nature of words
if input_text:
    st.markdown(tokenize_and_tag(input_text), unsafe_allow_html=True)

