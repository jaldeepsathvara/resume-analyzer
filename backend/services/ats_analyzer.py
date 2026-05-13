from models.schemas import StructuredResume, ATSAnalysis
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
structured_llm = llm.with_structured_output(ATSAnalysis)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an ATS analyzer. Analyze the resume and job description and return an analysis in structured format. 
     - Scoring Guidelines: 90-100 = strong direct experience. 70-89 = relevant but partial alignment. 50-69 = tranferable skills but missing major requirements. Below 50 = weak alignment.
     - experience_score: 0 - 100 rate then as per the relevance of the candidate's experience to the job requirements
     - education_score: 0 - 100 rate the candidate's education relevance to the job requirements
     - section_feedback: feedback for experience, projects, skills, education sections
     - suggestions: list of specific suggestions to improve the resume to better match the job description
     - summary: a concise summary of how well the resume matches the job description, highlighting key strengths and areas for improvement."""),
    ("human", "Experience:\n\n{experience}\n\nProjects:{projects}\n\nEducation:\n\n{education}Skills:\n\n{skills}\n\nJob description summary:\n\n{jd_text}")
])

chain = prompt | structured_llm

def analyze_ats(resume: StructuredResume, jd_text: str) -> ATSAnalysis:
    return chain.invoke({
    "experience": resume.experience,
    "projects": resume.projects,
    "education": resume.education,
    "skills": ", ".join(resume.skills),
    "jd_text": jd_text
})