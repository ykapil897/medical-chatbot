from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import runpy
from flags import ACTIVATE_SETTING_PINECONE
from src.setting_chatbot import chatbot

if(ACTIVATE_SETTING_PINECONE):
    runpy.run_path('medical-chatbot-using-groq/src/setting_pinecone.py')

qa = chatbot()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)


