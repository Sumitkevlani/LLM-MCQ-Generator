import os
import pandas as pd

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback

from dotenv import load_dotenv
from src.mcq_generator.logger import logging
from src.mcq_generator.utils import read_file,get_table_data


#Load environment variables from the .env file
load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")

#Create the llm object of OpenAI gpt-3.5-turbo model
llm = ChatOpenAI(openai_api_key=KEY,model='gpt-3.5-turbo',temperature=0.5)

#Create Quiz Generate Prompt template
TEMPLATE = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} multiple choice questions for {subject} subject with {tone} tone.
Make sure that the questions should not be repeated and check all the questions conforming the text as well.
Make sure you format your response like RESPONSE_JSON below and use it as a guide.
Ensure to make {number} MCQs.
### RESPONSE_JSON
{response_json}
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text","number","subject","tone","response_json"],
    template=TEMPLATE,
)

# Create LLM chain for the quiz prompt
quiz_chain = LLMChain(llm=llm,prompt=quiz_generation_prompt,output_key="quiz",verbose=True)

# Create Quiz Evaluation prompt template
EVALUATION_TEMPLATE = """
You are an expert grammarian and writer. Given a multiple choice quiz for {subject} subject.
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for the analysis. 
If the quiz is not as per the cognitive and thinkig ability of the student then update the quiz questions that need to be changed and change the tone such that it perfectly fits the student abilities.
Quiz_MCQs:
{quiz}
"""

quiz_evaluation_prompt = PromptTemplate(input_variables=["subject","quiz"],template=EVALUATION_TEMPLATE)

# Create LLM chain for the quiz evaluation prompt
review_chain = LLMChain(llm=llm,prompt=quiz_evaluation_prompt,output_key="review",verbose=True)

# Create Sequential Chain for the quiz generation and evaluation
generate_quiz_chain = SequentialChain(chains=[quiz_chain,review_chain],input_variables=["text","subject","number","tone","response_json"],output_variables=["quiz","review"],verbose=True)

