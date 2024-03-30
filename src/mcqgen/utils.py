import os
import PyPDF2
import json
import traceback
from src.mcqgen.logger import logging

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("error reading the PDF File")
            logging.log("Error Reading the File")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception(
            "unsupported file format only pdf and text file supported"
        )

def get_table_data(quiz_str):
    try:    
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value['mcq']
            option = [
                f"{option}:{option_value}"
                for option, option_value in value["options"].items()
                ]
        
            correct_answer = value['correct']
            quiz_table_data.append({"MCQ":mcq,"Choices":option,"Correct":correct_answer})

            return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e),e,e.__traceback__)
        return False