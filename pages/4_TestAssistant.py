import streamlit as st
import openai
import time
import config.pagesetup as ps
from openai import OpenAI
import uuid
from app import chat


#0. Page Config
st.set_page_config("FEOC Assistant1234", initial_sidebar_state="collapsed", layout="wide")

#1. Login and Page Setup

ps.set_title("FEOC", "FEOC Assistant")
ps.set_page_overview("Overview", "**FEOC Assistant** provides a way to quickly ask about the FEOC")

chat.app_chat()

