# 0. Import Libraries
import streamlit as st
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

# 1. Set Page Config
app_name = "FlowGenius AI"
page_title = "FlowGenius AI"
page_subtitle = "Page 2"
page_icon = "🌐☁️"
page_description = "Allows users to view page1."
overview_header = "Overview"
overview_text = f"**{page_subtitle}** {page_description.lower()}"

# 2. Set Page Title
ps.set_title(varTitle=page_title, varSubtitle=page_subtitle)

# 3. Set Page Overview
ps.set_page_overview(varHeader=overview_header, varText=overview_text)

# 4. Import variables
openai_api_key = st.secrets.openai.api_key



# 5. File upload
uploaded_file = st.file_uploader('Upload an article', type='txt')

# 6. Query text form
with st.form('my Form', clear_on_submit=True):
    query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.', disabled=not uploaded_file)
    # Form submission button
    submitted = st.form_submit_button('Submit')

# 7. Process form submission
if submitted and uploaded_file is not None:
    # Generate response from the uploaded file and query text
    with st.spinner('Calculating...'):
        response = generate_response(uploaded_file, openai_api_key, query_text)
        if response:
            st.info(response)
        else:
            st.error("Failed to generate a response. Please try again.")

def generate_response(uploaded_file, openai_api_key, query_text):
    # Load document if file is uploaded
    if uploaded_file is not None:
        documents = [uploaded_file.read().decode()]
        # Split documents into chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.create_documents(documents)
        # Select embeddings
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        # Create a vectorstore from documents
        db = Chroma.from_documents(texts, embeddings)
        # Create retriever interface
        retriever = db.as_retriever()
        # Create QA chain
        qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=openai_api_key), chain_type='stuff', retriever=retriever)
        return qa.run(query_text)

if len(result):
    st.info(response)
