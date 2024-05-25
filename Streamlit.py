import os
import pandas as pd
import json
import traceback
import streamlit as st
from dotenv import load_dotenv
from src.mcq_generator.logger import logging
from src.mcq_generator.MCQGenerator import generate_quiz_chain
from src.mcq_generator.utils import read_file,get_table_data
from langchain.callbacks import get_openai_callback

# Load Response.json
with open('Response.json','r') as file:
    RESPONSE_JSON = json.load(file)


# Create a title for the app
st.title("QuizQuest")

# Create a form
with st.form("user_inputs"):

    #Upload the file
    uploaded_file = st.file_uploader("Upload a PDF or Text File")
    
    #Numnber of Questions
    question_count = st.number_input("No. of MCQs",min_value=1,max_value=50)

    #Subject
    subject = st.text_input("Write the subject",max_chars=25)

    #Difficulty
    tone = st.selectbox("Complexity Level",("Easy","Medium","Hard"))

    #Generate Quiz
    submit_button = st.form_submit_button(label="Generate Quiz")


    # Check all the fields have value
    if submit_button and uploaded_file is not None and question_count and subject and tone:
        with st.spinner('Generating...'):
            try:
                TEXT = read_file(file=uploaded_file)

                #Generate Quiz
                with get_openai_callback() as cb:
                    response = generate_quiz_chain(
                        {
                            "text":TEXT,
                            "number":question_count,
                            "subject":subject,
                            "tone":tone,
                            "response_json":json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                logging.error(traceback.format_exc())
                st.error("Something went wrong")
                st.stop()

            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Total Cost: {cb.total_cost}")
                print(f"Completion Tokens: {cb.completion_tokens}")

                if(isinstance(response,dict)):
                    quiz = response["quiz"]

                    if quiz is not None:
                        table_data = get_table_data(quiz)

                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)

                            # Display review of the quiz
                            st.text_area(label="Review",value=response.get("review"))

                        else:
                            st.write("Error in the table data")

                else:
                    st.write(response)