from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from models.schemas import StructuredResume
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
structured_llm = llm.with_structured_output(StructuredResume)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a resume parser. Extract information from the resume text and return it in structured format.
     - skills: list all technical skills , tools, languages, frameworks
     - experience: summarize all work experience in one paragraph
     - projects: summarize all projects in one paragraph
     - education: summarize education in one paragraph
     Be through with skills extraction."""),
     ("human", "Resume text:\n\n{resume_text}")
])

chain = prompt | structured_llm

def parser_resume(resume_text: str) -> StructuredResume:
    return chain.invoke({"resume_text": resume_text})