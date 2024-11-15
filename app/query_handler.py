import pickle
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI
import os

def handle_query(query, file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            llm = OpenAI(temperature=0.9, max_tokens=500)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            return result
    return None
