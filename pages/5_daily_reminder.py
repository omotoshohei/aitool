import streamlit as st
import openai

ai_model = "gpt-4-turbo"
token = 4096

# Set the page title and favicon
st.set_page_config(page_title="Daily Reminder", page_icon=":bar_chart:")

openai.api_key = st.secrets['OPENAI_API_KEY']
st.title('Daily Reminder')




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
        en_input_topic = st.selectbox(
            "How are you feeling today?",
            ("I want to be more motivated", "I'm feeling sad", "I'm angry", "I just want to relax today"),
            index=0,  # Setting a default index if desired, or use None for no default selection
            key="en_input_topic"
        )

        en_input_reason = st.text_input(
            "What's the reason for this feeling? (e.g., 'I lost my motivation')", 
            key="en_input_reason"
        )

        en_input_plan = st.text_input(
            "What's your plan for today? (e.g., 'I'm going to meet my friends.')",
            key="en_input_plan"
        )

        if st.button("Generate a daily reminder", key="en_generate_quote"):
            # Create a prompt based on the user input
            en_prompt = f"""
            - Task: Select a unique quote each time and explain its relevance to the situation described. 
                Avoid repeating quotes and do not use quotes by Steve Jobs.
            - Feeling: {en_input_topic}.
            - Reason for the feeling: {en_input_reason}.
            - Plan for the day: {en_input_plan}.
            - Guidelines: Aim for quotes that are less commonly cited or consider a variety of cultural or historical sources to enhance diversity in selections.
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


        st.subheader('日本語')
        ja_input_topic = st.selectbox(
            "今日の気分を教えてください?",
            ("モチベーションを上げたい", "悲しい", "怒っている", "今はリラックスしたい"),
            index=0,  # Setting a default index if desired, or use None for no default selection
            key="ja_input_topic"
        )

        ja_input_reason = st.text_input(
            "その理由は何ですか？（例：「モチベーションが上がらない」）", 
            key="ja_input_reason"
        )

        ja_input_plan = st.text_input(
            "今日の予定は何ですか？（例：「友達と会う予定です」）",
            key="ja_input_plan"
        )

        if st.button("今日の名言を生成する", key="ja_generate_quote"):
            # Create a prompt based on the user input
            ja_prompt = f"""
            - Task: Select a unique quote each time and explain its relevance to the situation described in Japanese language. 
                Avoid repeating quotes and do not use quotes by Steve Jobs.
            - Feeling: {ja_input_topic}.
            - Reason for the feeling: {ja_input_reason}.
            - Plan for the day: {ja_input_plan}.
            - Guidelines: Aim for quotes that are less commonly cited or consider a variety of cultural or historical sources to enhance diversity in selections.
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