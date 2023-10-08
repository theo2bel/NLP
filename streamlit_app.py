import streamlit as st
import os
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import sentiwordnet as swn

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('sentiwordnet')

# Function to identify adverbs in a text
def identify_adverbs(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    adverbs = [word for word, pos in tagged_words if pos.startswith('RB')]
    return adverbs

# Function to score adverbs using SentiWordNet
def score_adverbs_with_swn(adverbs):
    adverb_scores = []
    for text in adverbs:
        score_text = []
        for adverb in text:
            synsets = list(swn.senti_synsets(adverb))
            if synsets:
                # Take the first synset as a simple example (you can combine multiple synsets)
                synset = synsets[0]
                positive_score = synset.pos_score()
                negative_score = synset.neg_score()
                objective_score = synset.obj_score()
                score_text.append((positive_score, negative_score, objective_score))
        adverb_scores.append(score_text)
    return adverb_scores

# Streamlit app
st.title("Text Positivity Calculator")

# Input text box
input_text = st.text_area("Enter text here:")

if input_text:
    # Identify adverbs in the input text
    adverbs = identify_adverbs(input_text)
    
    # Score the adverbs using SentiWordNet
    adverb_scores = score_adverbs_with_swn([adverbs])

    # Calculate the positivity score for the input text
    positivity_score = sum([float(i[0]) - float(i[1]) for i in adverb_scores[0]])

    st.write(f"Positivity Score: {positivity_score:.2f}")

