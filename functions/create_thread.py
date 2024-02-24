import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def new_thread():

    thread = client.beta.threads.create()

    thread_id = thread.id

    return thread_id