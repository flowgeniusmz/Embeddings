import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def run_check(varRunId: str, varThreadId: str):

    