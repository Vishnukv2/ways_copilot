import sys
import pysqlite3
sys.modules['sqlite3'] = pysqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import os
load_dotenv()
app = Flask(__name__)
CORS(app, resources={"/api/*": {"origins": "*"}})
api_key=os.getenv("OPENAI_API_KEY")
os.environ["openai_api_key"] = api_key

def get_vectorstore_from_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    vector_store = Chroma.from_documents(document_chunks, OpenAIEmbeddings())

    return vector_store

def get_context_retriever_chain(vector_store):
    llm = ChatOpenAI()
    
    retriever = vector_store.as_retriever()
    
    prompt = ChatPromptTemplate.from_messages([
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
      ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
    ])
    
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    
    return retriever_chain
    
def get_conversational_rag_chain(retriever_chain): 
    llm = ChatOpenAI()
    
    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are the Co-pilot of WaysAhead Global , you help the company's employees with coding and any questions they have regarding WaysAhead's projects. You answer their queries based on the context:\n\n{context}"),
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
    ])
    
    stuff_documents_chain = create_stuff_documents_chain(llm, prompt)
    
    return create_retrieval_chain(retriever_chain, stuff_documents_chain)

def get_response(user_input, vector_store, chat_history):
    retriever_chain = get_context_retriever_chain(vector_store)
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)
    
    response = conversation_rag_chain.invoke({
        "chat_history": chat_history,
        "input": user_input
    })
    
    return response['answer']

vector_store = None
chat_history = [AIMessage(content="Hello, I am a bot. How can I help you?")]

@app.route('/api/upload_doc', methods=['POST'])
def upload_pdf():
    global vector_store
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file:
            file_path = f"temp_{file.filename}"
            file.save(file_path)
            vector_store = get_vectorstore_from_pdf(file_path)
            os.remove(file_path)
            
            return jsonify({"message": "PDF processed successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ask', methods=['POST'])
def chat():
    global chat_history, vector_store
    if vector_store is None:
        return jsonify({"error": "PDF not uploaded or processed."}), 400
    data = request.json
    user_input = data.get('question')
    response = get_response(user_input, vector_store, chat_history)
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response))
    return jsonify({"response": response})
if __name__ == '__main__':
    app.run(debug=False)
