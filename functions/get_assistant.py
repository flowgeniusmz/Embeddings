import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def get_assistant_id():

    assistant_id = st.secrets.openai.assistant_id

    return assistant_id