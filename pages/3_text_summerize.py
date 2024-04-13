import streamlit as st
import openai

ai_model = "gpt-4-turbo"
token = 4096

# Set the page title and favicon
st.set_page_config(page_title="Summerize", page_icon=":bar_chart:")

openai.api_key = st.secrets['OPENAI_API_KEY']
st.title('Summerize')



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
        en_input = st.text_area("Enter your English text here:", key="en_input")
        if st.button("Summerize", key="en_summerize"):
            # Create a prompt based on the user input
            en_prompt = f"Summerize the following English sentence. Here is the text: {en_input}"
            # Make a request to the API to generate text
            en_response = openai.ChatCompletion.create(
                model=ai_model,  # Use the engine of your choice
                messages=[{"role": "user", "content": en_prompt}],
                max_tokens=token
            )
            st.write(en_response["choices"][0]["message"]["content"])

        st.text(" ")
        st.text(" ")


        st.subheader('Japanese')
        ja_input = st.text_area("Enter your Japanese text here:", key="ja_input")
        if st.button("Summerize", key="ja_summerize"):
            # Create a prompt based on the user input
            ja_prompt = f"Summerize the following English sentence. Here is the text: {ja_input}"
            # Make a request to the API to generate text
            ja_response = openai.ChatCompletion.create(
                model=ai_model,  # Use the engine of your choice
                messages=[{"role": "user", "content": ja_prompt}],
                max_tokens=token
            )
            st.write(ja_response["choices"][0]["message"]["content"])
    else:
        st.error("You have reached your maximum usage limit.")



























