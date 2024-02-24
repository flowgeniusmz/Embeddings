import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def new_thread_message(varThreadId: str, varMessageContent: str):

    message = client.beta.threads.messages.create(
        thread_id=varThreadId,
        content=varMessageContent
    )

    