from flask import Flask, request, jsonify
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain    
import os
load_dotenv()
app = Flask(__name__)
text_chunks = []

class PromptTemplate:
    def __init__(self, template):
        self.template = template

    def format(self, **kwargs):
        return self.template.format(**kwargs)

class SystemMessage:
    def __init__(self, content):
        self.content = content

    def to_json(self):
        return {"role": "system", "message": self.content}


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.5)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        chain_type="stuff",
    )
    return conversation_chain

@app.route('/upload_doc', methods=['POST'])
def upload_pdf():
    global text_chunks, conversation
    pdf_docs = request.files.getlist('pdf_docs')
    raw_text = get_pdf_text(pdf_docs)
    new_text_chunks = get_text_chunks(raw_text)
    text_chunks.extend(new_text_chunks)
    vectorstore = get_vectorstore(text_chunks)
    conversation = get_conversation_chain(vectorstore)
    return jsonify({'message': 'PDF uploaded and processed'})

@app.route('/ask', methods=['POST'])
def ask_question():
    user_question = request.json.get('question')
    system_message = SystemMessage("You are a co-pilot for WaysAhead Global. You are a coding assistant. You Have a vast knowledge about their projects and can help their employees to optimize their projects by providing them with snippets of code from the context")
    input_message = f"{system_message.to_json()}\n{user_question}"
    response = conversation.invoke({'question': input_message})
    latest_ai_message = None
    for message in response['chat_history']:
        if message.type == 'ai':
            latest_ai_message = message
    if latest_ai_message:
        return jsonify({'response': latest_ai_message.content})
    else:
        return jsonify({'error': 'No AI response found'})

if __name__ == '__main__':
    app.run(debug=False)
