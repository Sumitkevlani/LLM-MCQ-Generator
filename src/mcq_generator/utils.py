import os
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error in reading the PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("Only .txt and .pdf files are supported")
    


def get_table_data(quiz):
    try:
        print(quiz)
        quiz_dict = json.loads(quiz)
        quiz_table_data = []

        for key,value in quiz_dict.items():
            question = value["question"]
            options = " | ".join(
                [
                    f"{option}:{option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append({"question":question,"options":options,"correct":correct})
        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e),e,e.__traceback__)
        return False