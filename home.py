import streamlit as st

# Page Configuration
st.set_page_config(page_title="AI Text Assistant", page_icon=":memo:")

# Welcome Message
st.title("Welcome to AI Text Assistant")
st.subheader("Your go-to solution for AI-powered text processing and language services.")

# Feature Overview
st.markdown("""
## Features
Explore the range of services our app offers:
- **Article Generator**: Generate insightful articles on a variety of topics.
- **Code Debug**: Analyze and debug your code efficiently.
- **Correction**: Enhance your text with our advanced correction tool.
- **Translation**: Translate your content into multiple languages.
- **Summarization**: Condense long texts into concise, informative summaries.
""")

# Feature Navigation
st.markdown("## Get Started")

# Initialize the session state for 'authenticated' key
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
password_key = st.secrets['PASSWORD']

# Only show the login form if the user is not authenticated
if not st.session_state['authenticated']:
    password_placeholder = st.empty()
    login_button_placeholder = st.empty()

    password = password_placeholder.text_input("Enter your password", type="password")

    if login_button_placeholder.button('Login'):
        if password == password_key:
            st.session_state['authenticated'] = True
            password_placeholder.empty()
            login_button_placeholder.empty()
            st.success("Login successful!")  # Provide immediate feedback on successful login
        else:
            st.error('Wrong password')

# If authenticated, show the main page content
if st.session_state['authenticated']:
    st.markdown("""
    You are logged in. Navigate using the menu on the sidebar.
    """)
# else:
#     # If not authenticated, show a warning
#     st.warning('Please enter your password and click login to continue.')



