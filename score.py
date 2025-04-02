!pip install readability

import os
import streamlit as st
from readability import Readability
import nltk

# Set and ensure NLTK data directory
nltk_data_dir = 'C:/nltk_data'
os.environ['NLTK_DATA'] = nltk_data_dir
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.download('punkt', download_dir=nltk_data_dir)

# App UI
st.title("📚 Flesch-Kincaid Grade Level Checker")
st.write("Paste your text below (minimum 100 words recommended):")

# Text input
text_input = st.text_area("Enter your text here:", height=300)

# Submit button
if st.button("Submit"):
    if text_input.strip():
        try:
            r = Readability(text_input)
            fk = r.flesch_kincaid()
            st.success("✅ Flesch-Kincaid Grade Level Result")
            st.write(f"**Score:** {fk.score:.2f}")
            st.write(f"**Grade Level:** {fk.grade_level}")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter some text before submitting.")
