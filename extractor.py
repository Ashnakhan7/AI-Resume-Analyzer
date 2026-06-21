import pdfplumber

def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text

    return text

from skills import skills_list

def extract_skills(text):

    found = []

    text = text.lower()

    for skill in skills_list:

        if skill in text:

            found.append(skill)

    return found

import re

def extract_email(text):

    pattern = r'\S+@\S+'

    emails = re.findall(pattern, text)

    return emails
