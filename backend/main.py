from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import ResumeAnalysisResponse
from services.resume_parser import parser_resume
from services.pdf_extractor import extract_text_from_pdf
from services.skill_extractor import parser_job_description
from services.keyword_matcher import match_keywords
from services.scorer import scorer
from services.ats_analyzer import analyze_ats
import io
import os

app = FastAPI()

hf_token = os.getenv("HF_TOKEN")
if hf_token:
    os.environ["HUGGINGFACE_HUB_TOKEN"] = hf_token

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_resume(file: UploadFile = File(...), jd_text: str = Form(...)):
    file_bytes = io.BytesIO(await file.read())
    text = extract_text_from_pdf(file_bytes)
    resume = parser_resume(text)
    jd_skills = parser_job_description(jd_text)
    keyword_match = match_keywords(resume.skills, jd_skills.skills)
    ats_analysis = analyze_ats(resume, jd_text)
    match_score = scorer(keyword_match["score"], ats_analysis)
    return ResumeAnalysisResponse(
        match_score=match_score,
        keyword_match=keyword_match["score"],
        experience_score=ats_analysis.experience_score,
        education_score=ats_analysis.education_score,
        matched_skills=keyword_match["matched_skills"],
        missing_skills=keyword_match["missing_skills"],
        section_feedback=ats_analysis.section_feedback,
        suggestions=ats_analysis.suggestions,
        summary=ats_analysis.summary
    )