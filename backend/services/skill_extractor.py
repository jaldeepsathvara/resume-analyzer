from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from models.schemas import SkillList
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
structured_llm = llm.with_structured_output(SkillList)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a skill extractor. Extract information from the job description text and return it in a structured format. Do not extract generic responsibilities, tasks, or soft skills. Only extract concrete technical skills, frameworks, tools, libraries, databases, AI concepts, and programming technologies.
     - skills: list all technical skills , tools, languages, frameworks
     Be through with skills extraction."""),
    ("human", "Job description:\n\n{job_description}")
])

chain = prompt | structured_llm

def parser_job_description(job_description: str) -> SkillList:
    return chain.invoke({"job_description": job_description})