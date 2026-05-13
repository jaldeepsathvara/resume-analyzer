from models.schemas import ATSAnalysis

def scorer(keyword_match: int, ats_analysis: ATSAnalysis) -> float:
    match_score = (keyword_match * 0.4) + (ats_analysis.experience_score * 0.35) + (ats_analysis.education_score * 0.25)
    return round(match_score)