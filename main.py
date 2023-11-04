import streamlit as st
import PyPDF2
import openai
import requests
import json
import math
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text


def extract_info(text):
    api_key = "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"
    openai.api_key = api_key
    prompt = """Provide a a summary report, strengths and weaknesses in the
    resume, and on what areas the user can work to improve their resume
    of the based on the domain of the user : """ + text
    response = openai.Completion.create(
        model='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=2000,
        top_p=0.2
    )
    return response.choices[0].text


def main():
    st.title("Resume Analyzer")
    st.write("Upload a PDF resume for analysis.")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.write("Analyzing the uploaded resume...")

        resume_text = extract_text_from_pdf(uploaded_file)

        info = extract_info(resume_text)

        st.subheader("Extracted Text:")
        st.markdown(f"<div style='overflow-x: hidden;'>{info}</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
