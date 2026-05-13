from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def match_keywords(resume_skills: list[str], jd_skills: list[str], threshold: float = 0.55):
    if not jd_skills:
        return {"score": 0, "matched_skills": [], "missing_skills": []}

    if not resume_skills:
        return {"score": 0, "matched_skills": [], "missing_skills": jd_skills}

    resume_embeddings = model.encode(resume_skills)
    jd_embeddings = model.encode(jd_skills)

    similarity_matrix = cosine_similarity(jd_embeddings, resume_embeddings)

    matched_skills = []
    missing_skills = []

    for i, row in enumerate(similarity_matrix):
        best_score = np.max(row)

        if best_score >= threshold:
            matched_skills.append(jd_skills[i])
        else:
            missing_skills.append(jd_skills[i])

    keyword_match_score = (len(matched_skills) / len(jd_skills)) * 100

    return {
        "score": round(keyword_match_score),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }