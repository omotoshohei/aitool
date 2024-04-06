import streamlit as st
import openai


openai.api_key = st.secrets['OPENAI_API_KEY']

# Create a prompt based on the top complaints for the restaurant
prompt = f"Translate from Japanese to English. こんにちは。"
# Make a request to the API to generate text
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use the engine of your choice
    messages = [{"role": "user", "content": prompt}],
    max_tokens = 100
)

st.write(response["choices"][0]["message"]["content"])
