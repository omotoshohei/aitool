import streamlit as st
import openai

ai_model = "gpt-4-0125-preview"
token = 4096

# Set the page title and favicon
st.set_page_config(page_title="Joke Generator", page_icon=":bar_chart:")

openai.api_key = st.secrets['OPENAI_API_KEY']
st.title('Joke Generator')




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
        en_input_topic = st.text_input("Topic（e.g. Sunday）", key="en_input_topic")
        en_input_occupation = st.text_input("Your Occupation(e.g. Data Scientist)", key="en_input_occupation")
        # en_input_message = st.text_input("What do you want to say? (e.g. prepare for tomorrow)", key="en_input_message")

        if st.button("Generate a rap", key="en_generate_rap"):
            # Create a prompt based on the user input
            en_prompt = f"""
            - Task： Generate 5 jokes in English
            - Topic：{en_input_topic}。
            - Occupation： {en_input_occupation}。
            """
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
        ja_input_topic = st.text_input("Topic（e.g. 日曜日）", key="ja_input_topic")
        ja_input_occupation = st.text_input("Your Occupation(e.g. データサイエンティスト)", key="ja_input_occupation")
        # ja_input_message = st.text_input("What do you want to say? (e.g. prepare for tomorrow)", key="ja_input_message")

        if st.button("Generate a rap", key="ja_generate_rap"):
            # Create a prompt based on the user input
            ja_prompt = f"""
            - 依頼： 日本語で５つのジョークを生成ください。
            - トピック：{ja_input_topic}。
            - 仕事内容： {ja_input_occupation}。
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