import streamlit as st

#Upload PDF files
st.header("My first Chatbot")
with st.sidebar:
    st.title("Your Documents")
text= st.text_input("Enter your name")
file = st.file_uploader(" Upload a PDf file and start asking questions",type="pdf")
