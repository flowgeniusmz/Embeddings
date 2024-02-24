import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def new_thread_run(varAssistantId: str, varThreadId: str):

    run = client.beta.threads.runs.create(
        thread_id=varThreadId,
        assistant_id=varAssistantId
    )

    run_id = run.id

    return run_id

