from pydantic import BaseModel

class StructuredResume(BaseModel):
    skills: list[str]
    experience: str
    projects: str
    education: str

class SkillList(BaseModel):
    skills: list[str]

class SectionFeedback(BaseModel):
    experience: str
    projects: str
    skills: str
    education: str

class ATSAnalysis(BaseModel):
    experience_score: int
    education_score: int
    section_feedback: SectionFeedback
    suggestions: list[str]
    summary: str

class ResumeAnalysisResponse(BaseModel):
    match_score: int
    keyword_match: int
    experience_score: int
    education_score: int
    matched_skills: list[str]
    missing_skills: list[str]
    section_feedback: SectionFeedback
    suggestions: list[str]
    summary: str