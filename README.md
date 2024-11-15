# Article-Analysis-and-Answer-Generation

This project leverages OpenAI's GPT for **semantic search** and **question answering** on news articles. It allows users to input URLs of news articles and ask questions, which the system answers based on the content of the provided articles, with source attribution.

## Features

- **Semantic Search**: Retrieves relevant information from multiple news articles.
- **Question Answering**: Users can ask questions, and the system provides contextually relevant answers based on the provided news articles.
- **Source Attribution**: Answers include the source URLs from which information is retrieved.
- **Embedding-based Retrieval**: Uses OpenAI's embeddings to convert text into numerical representations for efficient retrieval and answering.

## Installation

To run the project, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/omaar25/Article-Analysis-and-Answer-Generation.git
cd Article-Analysis-and-Answer-Generation
pip install -r requirements.txt
```
### 2.Set up your .env file
Make sure to add your OpenAI API key in a .env file:
```bash
OPENAI_API_KEY=your_openai_api_key
```

## Usage
Provide URLs: In the sidebar, input up to 3 URLs of news articles you wish to analyze.
Ask a Question: Enter a question related to the content of the articles.
Receive Answer: The tool will retrieve relevant information and provide an answer with source attribution.

## Dependencies
Streamlit: For the web interface.
LangChain: For integrating with OpenAI and managing workflows.
FAISS: For vector-based similarity search.
OpenAI: For GPT-based text generation and embeddings.
