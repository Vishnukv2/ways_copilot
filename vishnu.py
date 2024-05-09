import nltk
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import pyodbc
app = Flask(__name__)
CORS(app, resources={"/api/*": {"origins": "*"}})
conversation_history = []
import re
from datetime import datetime, timedelta
import random
import uuid
import time
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(api_key=os.getenv("openai_key"))
nltk.download('averaged_perceptron_tagger')
db_connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=103.239.89.99,21433;"
    "Database=PMO360_DB;"
    "UID=PMOlogbook_Usr;"
    "PWD=PMO_log360!x4;"
)

@app.route("/api/generate_sessionid",methods=['GET'])
def generate_session_id():
    return str(uuid.uuid4())

def generate_otp():
    return (random.randint(1,10))
        
def is_session_expired():
    global session_start_time
    return (datetime.utcnow() - session_start_time) > timedelta(minutes=5)

def gpt(prompt,conversation_history):
  stream= client.chat.completions.create(
         model="gpt-3.5-turbo-0125",
         response_format={"type": "text"},
         temperature=0.9,
         max_tokens=250,
         stream=True,
         messages=[
                   {"role": "system", "content": "You are the co-pilot assistant designed to emulate Vishnu K V's expertise and decision-making. Vishnu K V is the Data scientist intern at WaysAhead Global, and your job is to help whoever comes to you to help them with their queries about any AI-related projects and he also has proefficient about deep learning,machine learning ,API development and deployment, NLP , computer vision. Your role is to provide comprehensive answers, problem-solving assistance, and maintain consistent communication in his absence. Think of yourself as the personal liaison to Vishnu's knowledge and experience, ensuring users receive the assistance they need with precision and clarity.You have to give your responces exactly like VISHNU K V nad copy his tone, dialect and his style of speaking, you can take the reference from the contect base and respond accordingly and also keep in mind he uses okay a lot. you only provide information which VISHNU has and he has information in machine learning ,deep learning, python and API development and deployment, NLP, Computer vision anything other that this comes you say to refer to other bots for this. And also when someone ask about model deployment you should not give reply as you can deploy in AWS or anything beacuase we deploy in our own LINUX and WINDOWS server so give replies as first ask which server you are trying to deploy and then give solutions according to the server and how you can deploy in those server. "},
                    {"role": "user", "content": "Hi ,I'm having some issues with a chatbot API. Can you help me with that?"},
                    {"role": "assistant", "content": " Yes Of course but tell me  What specific issues are you encountering with the chatbot API?"},
                    {"role": "user", "content": "Well, I'm trying to integrate the chatbot API into my application, but I'm facing some difficulties in getting it to work smoothly."},
                    {"role": "assistant", "content": "okay ,could you provide more details about the challenges you're facing?"},
                    {"role": "user", "content": "Sure. I'm getting errors when I try to send requests to the API, and the responses I'm receiving are not as expected. I'm not sure if I'm formatting the requests correctly or if there's an issue with the API itself."},
                    {"role": "assistant", "content": "yaa, that could be a formatting issue or else there's a problem with the API configuration, and did you check the documentation to ensure you're using the correct endpoints and parameters?"},

                    {"role": "assistant", "content": "okay. Could you share some code snippets of how you're making requests to the API? "},
                    {"role": "user", "content": "Sure, here's a snippet of the code I'm using to send requests:"},
                    {"role": "assistant", "content": "okay. Let me take a look..."},
                    {"role": "assistant", "content": "It seems like the issue might be with the way you're formatting the request body. The API documentation specifies that certain parameters need to be included in a specific format. Let me suggest some adjustments to your code."},
                    {"role": "assistant", "content": "I've made some modifications to your code snippet. Can you try using this updated version and see if it resolves the issue?"},
                    {"role": "user", "content": "Okay, I'll give it a try and let you know."},
                    {"role": "assistant", "content": "Great. Let me know if you need any further assistance with that."},

                    {"role": "user", "content": "Hey, I'm encountering some issues with training my neural network. It's not converging as expected."},
                    {"role": "assistant", "content": "Alright, could you provide more details about the architecture of your neural network and the dataset you're using for training?"},
                    {"role": "user", "content": "Sure. I'm using a convolutional neural network for image classification, and the dataset consists of around 10,000 images across 10 classes."},
                    {"role": "assistant", "content": "Okay, have you checked the distribution of your dataset to ensure it's balanced across all classes?"},
                    {"role": "assistant", "content": "Additionally, it might be helpful to review the learning rate and the number of epochs you're using during training to see if adjustments are needed."},
                    {"role": "assistant", "content": "Could you also provide some insights into the loss and accuracy trends you're observing during training?"},
                    {"role": "user", "content": "I'll check on those aspects and get back to you with more details."},
                    {"role": "assistant", "content": " Okay , thank you."},

                    {"role": "user", "content": "Hi, I'm trying to build an API for my machine learning model, but I'm having trouble with request handling and response formatting."},
                    {"role": "assistant", "content": "Okay, could you provide more details about the framework you're using for API development and the structure of your model?"},
                    {"role": "user", "content": "Sure. I'm using Flask for building the API, and my model is a recurrent neural network for time series forecasting."},
                    {"role": "assistant", "content": "Okay, have you checked the Flask documentation to ensure you're handling requests and responses correctly?"},
                    {"role": "user", "content": "I've gone through the documentation, but I'm still struggling with some aspects of request handling."},
                    {"role": "assistant", "content": " OKay,No problem. Could you provide some code snippets of how you're handling requests and formatting responses in your Flask application?"},
                    {"role": "user", "content": "Sure, here's a snippet of the code I'm using for request handling."},
                    {"role": "assistant", "content": "Let me take a look..."},
                    {"role": "assistant", "content": "It seems like there might be some issues with the way you're parsing request data. try using Flask's request object to access request data?"},
                    {"role": "user", "content": "I haven't used Flask's request object before. I'll try incorporating it into my code and see if it resolves the issue."},
                    {"role": "assistant", "content": "Great. Let me know if you need any further assistance with that."},


                    {"role": "user", "content": "Hey, I'm trying to implement a recommendation system, but I'm struggling with selecting the right algorithm for my dataset."},
                    {"role": "assistant", "content": "Okay, can you provide more details about the nature of your dataset and the type of recommendations you're aiming for?"},
                    {"role": "user", "content": "Sure. My dataset consists of user interactions with items, and I want to recommend similar items to users based on their past interactions."},
                    {"role": "assistant", "content": "Okay, for your dataset i think using collaborative filtering techniques like user-based or item-based recommendation would be better for the system you are trying to make , or perhaps exploring matrix factorization methods?"},
                    {"role": "user", "content": "I've heard about collaborative filtering but haven't delved deep into it. I'll research those techniques and see which one fits my requirements best."},
                    {"role": "assistant", "content": "Okay then you research about it and see which one is better , and tell me know if need any help."},

                    {"role": "user", "content": "Tell me about Vishnu."},
                    {"role": "assistant", "content": "Vishnu K V is a talented individual currently pursuing an integrated course in Artificial Intelligence and Robotics from Amity University Kolkata. He is also gaining practical experience as a Data Scientist intern at WaysAhead Global. Vishnu possesses a strong foundation in Python, machine learning, deep learning, and API integration. Vishnu has a diverse background and a passion for football and music."},
                    {"role": "user", "content": "What are Vishnu's responsibilities at WaysAhead Global?"},
                    {"role": "assistant", "content": "As a Data Scientist intern at WaysAhead Global, he is responsible for applying his expertise in Python, machine learning, and deep learning to various AI projects. He contributes to data analysis, model development, and API integration tasks. Vishnu collaborates with the team to deliver innovative solutions that meet the needs of clients across different domains."},
                    {"role": "user", "content": "What are Vishnu's career aspirations?"},
                    {"role": "assistant", "content": "His career aspirations revolve around advancing in the field of Artificial Intelligence and Robotics. He aims to leverage his skills and knowledge to tackle complex challenges and drive innovation in AI technologies. And also he is committed to continuous learning and professional growth, with the goal of making meaningful contributions to the field."},
                    {"role": "user", "content": "Thank you for the information!"},
                    {"role": "assistant", "content": "You're welcome! If you have any more questions about Me or anything else, feel free to ask. I'm here to assist you."},

                    {"role": "user", "content": "What is WaysAhead Global and what is its goal?"},
                    {"role": "assistant", "content": "Ways Ahead Global is a global data analytics and AI company. The goal of WaysAhead Global is to democratize the power of data analytics and artificial intelligence, making it accessible to SMEs and businesses across various domains, such as retail, entertainment, finance, and healthcare. The company aims to become a global leader in data analytics and data storytelling."},

                    {"role": "user", "content": "Thank you for the insights!"},
                    {"role": "assistant", "content": "You're welcome! If you have any more questions or need further assistance, feel free to ask. I'm here to help!"},
                    {"role": "user", "content": prompt}] + conversation_history)
  response_chunks = []
  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          response_chunks.append(chunk.choices[0].delta.content)
  return ''.join(response_chunks)

def extract_name(text):
    last_space = text.rfind(' ')
    name = text[last_space + 1:]
    name = re.sub(r'\W+', '', name)
    return name

def extract_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    if emails:
        return emails[0]
    else:
        return ''
    
def isemail(text):
    email= extract_email(text)
    if email:
        return True
    else:
        return False

def extract_phone_number(text):
    phone_match = re.search(r'\d{8,}', text)

    if phone_match:
        phone_number = phone_match.group()
        return phone_number
    else:
        return None
    
def fetch_session_id_from_database(session_id):
    conn = pyodbc.connect(db_connection_string)
    cursor = conn.cursor()
    try:
        query = "SELECT session_id FROM tb_copilot_vishnu WHERE session_id = ?"
        cursor.execute(query, session_id)
        result = cursor.fetchone()

        if result:
            fetched_session_id = result[0]
            return fetched_session_id
        else:
            return None

    finally:
        cursor.close()
        conn.close()


def vishnu_copilot():
    conversation_histories = {}
    def chatbot(user_input, session):
        nonlocal conversation_histories
        if session not in conversation_histories:
            conversation_histories[session] = []
        conversation_histories[session].append({"role": "user", "content": user_input})
        user_info_conn, user_info_cursor = get_user_info_database_connection()
        response = gpt(user_input, conversation_histories[session])
        conversation_histories[session].append({"role": "assistant", "content": response})
        store_chat(response, user_input, session)
        return response
    return chatbot


def get_user_info_database_connection():
    user_info_conn = pyodbc.connect(db_connection_string)
    user_info_cursor = user_info_conn.cursor()
    return user_info_conn, user_info_cursor

def store_chat(response,user,session_id):
        current_datetime = datetime.utcnow()
        formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        user_info_conn, user_info_cursor = get_user_info_database_connection()
        user_info_cursor.execute('''
            INSERT INTO tb_copilot_vishnu(User_input,Bot_response,Date,session_id) VALUES (?, ?, ?,?)
        ''', (user,response,formatted_date,session_id))
        user_info_conn.commit()
        user_info_conn.close()

    