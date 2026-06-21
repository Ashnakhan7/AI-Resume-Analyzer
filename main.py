from extractor import extract_text
from extractor import extract_email
from extractor import extract_skills

# Read resume

resume_text = extract_text("resume.pdf")

# Extract email

emails = extract_email(resume_text)

# Extract skills

resume_skills = extract_skills(resume_text)

print("Email:")

print(emails)

print()

print("Skills Found:")

print(resume_skills)

# Read job description

with open("job_description.txt", "r") as f:
    job_text = f.read().lower()

job_skills = extract_skills(job_text)

resume_set = set(resume_skills)
job_set = set(job_skills)

matched = resume_set & job_set

score = (len(matched) / len(job_set)) * 100

print("\nResume Score:")

print(f"{score:.2f}%")

print("\nMatched Skills:")

print(matched)

print("\nMissing Skills:")

print(job_set - resume_set)