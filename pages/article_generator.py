import streamlit as st
import openai

ai_model = "gpt-4-0125-preview"
token = 4096

# Set the page title and favicon
st.set_page_config(page_title="Article Generator", page_icon=":bar_chart:")

openai.api_key = st.secrets['OPENAI_API_KEY']
st.title('Article Generator')




# Initialize the session state for 'authenticated' key
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if 'usage_count' not in st.session_state:
    st.session_state['usage_count'] = 0  # Usage counter

password_key = st.secrets['PASSWORD']

# Only show the login form if the user is not authenticated
if not st.session_state['authenticated']:
    password_placeholder = st.empty()
    login_button_placeholder = st.empty()

    password = password_placeholder.text_input("Enter your password", type="password")

    if login_button_placeholder.button('Login'):
        if password == password_key:
            st.session_state['authenticated'] = True
            st.session_state['usage_count'] = 0  # Reset the usage count upon new login
            password_placeholder.empty()
            login_button_placeholder.empty()
            st.success("Login successful!")
        else:
            st.error('Wrong password')

# If authenticated, show the main page content
if st.session_state['authenticated']:
    # Define a maximum number of uses
    max_uses = 3

    if st.session_state['usage_count'] < max_uses:
        # Main Contents Start from here -------------------------------

        st.subheader('English')
        en_input = st.text_input("Enter the topic here in English:(e.g. generative ai, etc)", key="en_input")
        if st.button("Generate Article", key="en_generate_article"):
            # Create a prompt based on the user input
            en_prompt = f"""
            Generate the blog article with the following topic. 
            The language is in English. 
            The max-token is {token}, so complete the sentence within the token.
            Here is the topic: {en_input}
            """
            # Make a request to the API to generate text
            en_response = openai.ChatCompletion.create(
                model=ai_model,  # Use the engine of your choice
                messages=[{"role": "user", "content": en_prompt}],
                max_tokens= token
            )
            st.write(en_response["choices"][0]["message"]["content"])

        st.text(" ")
        st.text(" ")


        st.subheader('Japanese')
        ja_input = st.text_input("Enter the topic here in English:(e.g. 生成AI, etc)", key="ja_input")
        if st.button("Generate Article", key="ja_generate_article"):
            # Create a prompt based on the user input
            ja_prompt = f"""
            Generate the blog article with the following topic. 
            The language is in Japanese. 
            The max-token is {token}, so complete the sentence within the token.
            Here is the topic: {ja_input}
            """
            # Make a request to the API to generate text
            ja_response = openai.ChatCompletion.create(
                model=ai_model,  # Use the engine of your choice
                messages=[{"role": "user", "content": ja_prompt}],
                max_tokens=token
            )
            st.write(ja_response["choices"][0]["message"]["content"])
    else:
        st.error("You have reached your maximum usage limit.")














