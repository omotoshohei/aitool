import streamlit as st
import openai

ai_model = "gpt-4-turbo"
token = 4096

# Set the page title and favicon
st.set_page_config(page_title="Anger Management", page_icon=":bar_chart:")

openai.api_key = st.secrets['OPENAI_API_KEY']
st.title('Anger Management')




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
        en_input_who = st.selectbox("Who are you angry at?",("Your boss", "Your co-worker", "Your partner", "Your family or relatives", "Your friend"),index=None,placeholder="Select contact method...", key="en_input_who")
        en_input_level = st.selectbox("Your anger level",("1", "2", "3", "4", "5"),index=None,placeholder="How much are you angry out of 5?", key="en_input_level")
        en_input_situation = st.text_input("Explain the situation (e.g. My boss gives me too much work to handle.)", key="en_input_situation")

        if st.button("Get an advice", key="en_generate_adivce"):
            # Create a prompt based on the user input
            en_prompt = f"""
            - Task： you are a psychological counselor. Please give an advice for this situation.
            - Situation：{en_input_who}.
            - Anger level:{en_input_level}
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
        ja_input_who = st.selectbox("Who are you angry at?",("Your boss", "Your co-worker", "Your partner", "Your family or relatives", "Your friend"),index=None,placeholder="Select contact method...", key="ja_input_who")
        ja_input_level = st.selectbox("Your anger level",("1", "2", "3", "4", "5"),index=None,placeholder="How much are you angry out of 5?", key="ja_input_level")
        ja_input_situation = st.text_input("Explain the situation (e.g. My boss gives me too much work to handle.)", key="ja_input_situation")

        if st.button("Get an advice", key="ja_generate_adivce"):
            # Create a prompt based on the user input
            ja_prompt = f"""
            - Task： you are a psychological counselor. Please give an advice for this situation in Japanese
            - Situation：{ja_input_who}.
            - Anger level:{ja_input_level}
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