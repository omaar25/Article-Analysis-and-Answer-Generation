# main.py
import streamlit as st
from app.loader import process_urls
from app.embeddings import create_embeddings
from app.query_handler import handle_query
from config.settings import FAISS_FILE_PATH
import pickle

st.title(" Research Tool ")
st.sidebar.title("News Article URLs")

urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
process_url_clicked = st.sidebar.button("Process URLs")

if process_url_clicked:
    data = process_urls(urls)
    vectorstore = create_embeddings(data)
    with open(FAISS_FILE_PATH, "wb") as f:
        pickle.dump(vectorstore, f)

query = st.text_input("Ask a question:")
if query:
    result = handle_query(query, FAISS_FILE_PATH)
    if result:
        st.header("Answer")
        st.write(result["answer"])
        st.subheader("Sources")
        for source in result.get("sources", "").split("\n"):
            st.write(source)
