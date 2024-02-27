#deanslist.py

#Imports
import openai
from openai import OpenAI
import time
import streamlit as st
from config import pagesetup as ps
from app import chat


# 0. Set Page Config
app_title = "Dean's Assistant"
app_icon = "🎓"
app_sidebar = "collapsed"
app_layout = "wide"
page_title = "Dean's Assistant"
page_subtitle = "John F Kennedy Middle School"

st.set_page_config(page_title=app_title, page_icon=app_icon, initial_sidebar_state=app_sidebar, layout=app_layout)


# 1. Set Session State (Initialize session state for storing questions and responses if not already done)
if 'messages' not in st.session_state:
    st.session_state.messages = []

if "initial_messages" not in st.session_state:
    st.session_state.initial_messages = [
        {"role": "assistant", "content": "I am your Dean's assistant! How can I help you?"}
    ]

if "q_and_a" not in st.session_state:
    st.session_state.q_and_a = []

# 2. Set Page Title
#ps.set_title(page_title, page_subtitle)

# 3. Set Variables
client = OpenAI(api_key=st.secrets.openai.api_key)
assistantid = st.secrets.openai.assistant_key_3
thread = client.beta.threads.create()
threadid = thread.id
    
#Streamlit App Title
title_container = st.container()
with title_container:
    cc = st.columns(2)
    with cc[0]:
        st.title('Dean\'s Assistant')
    with cc[1]:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQroYsyWjvZmkyguxf2_XUKqcWTNLkZrRbPzPL8MU5I&s', caption='Plainfield School District 202') #Streamlit image for branding

# Streamlit Overview Section
overview_container = st.container()
with overview_container:
    ps.set_page_overview(varHeader="Overview", varText="The **Dean's Assistant** presented by FlowGenius is an AI assistant that has been trained on everything about your school.")
st.divider()
chat.app_chat()
#MAIN FUNCTIONALITY
st.divider()


# Add a Streamlit footer
footer_html = """
<div style='position: absolute; bottom: 0; left: 0; width: 100%; text-align: right; padding: 10px;'>
    <p style='margin: 0;'>Powered by FlowGenius</p>
    <img src='https://media.licdn.com/dms/image/D5603AQGzpMfnqrHpvA/profile-displayphoto-shrink_800_800/0/1691028781928?e=2147483647&v=beta&t=DR35TiCIcWT711AOyjHTsWIf2E2L0t_ktfGDqrqSYiE' style='height: 50px; margin-top: 5px;'/>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
