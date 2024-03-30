import os
import json
import pandas as pd
import traceback
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
from src.mcqgen.logger import logging

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
PROMPT = """
Text : {text}
You are an expert MCQ Generator. GIven the above text, it is your job to
create a quiz of {number} multiple choice questioin for {subject} students
in {tone} tone. Make Sure the question are not repeated and check all the questions
to be conforming the text as well as Make sure to format response like RESPONSE_JSON below and use it as a guide.\
ENsure to make {number} MCQ
###RESPONSE JSON 
{response_json}

In the output provide a clean json do not use "###RESPONSE JSON " or "\n" in final output of json file
Do not use "\'machine learning\'" in final output directly use "machine learning" no need to use \'\' in final output
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text","number","subject","tone","response_json"],
    template=PROMPT
)
quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz",verbose=True)
 
