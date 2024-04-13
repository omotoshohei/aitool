import streamlit as st

# Page Configuration
st.set_page_config(page_title="AI Text Assistant", page_icon=":memo:")

# Welcome Message
st.title("Less Prompt")
st.subheader("Minimal Input, Maximum Output")

# Feature Overview
st.markdown("""
## Features
At Less Prompt, we believe in simplicity. Our cutting-edge AI understands your needs with just a few words, turning brief interactions into comprehensive results.
- **Variety of templates**: Choose the template that best fits your needs.
- **Optimized Prompts**: Each template comes with the most effective prompt already installed.
- **Customizable**: Enhance your text with our advanced correction tools.
- **Password Protection**: Users must enter a password to access the tool, protecting against unauthorized use and ensuring charges are made only to intended users.
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
# Feature Overview
st.markdown("""
## Developper
- [Shohei Omoto](https://heysho.com)
- SEO, Data, Digital Marketing Specialist based in Tokyo, Japan.
""")
st.markdown("""
## Please Note
- For inquiries on using this template, please reach out to [Shohei Omoto](https://heysho.com).
- Please note that unauthorized reproduction or use is prohibited.
""")

