import streamlit as st
import requests

st.title("LLaMA Text Summarizer")

with st.form("summarize_form"):
    user_input = st.text_area(
        "Enter your text here:", 
        height=300,
        help="Press Ctrl+Enter to submit"
    )
    submitted = st.form_submit_button("Summarize")
    
    if submitted:
        if not user_input.strip():
            st.warning("Paste or type some text first.")
        else:
            with st.spinner("Generating summary..."):
                try:
                    r = requests.post("http://localhost:8000/summarize/", data={"text": user_input}, timeout=60)
                    r.raise_for_status()
                    summary = r.json().get("summary", "No summary returned.")
                except Exception as e:
                    summary = f"Error: {e}"
            st.subheader("Summary")
            st.write(summary)
