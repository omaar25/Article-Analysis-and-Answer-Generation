from langchain.document_loaders import UnstructuredURLLoader
import time

def process_urls(urls):
    loader = UnstructuredURLLoader(urls=urls)
    time.sleep(2)  
    data = loader.load()
    return data
