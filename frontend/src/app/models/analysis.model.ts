export interface SectionFeedback {
  experience: string;
  projects: string;
  skills: string;
  education: string;
}

export interface ResumeAnalysis {
  match_score: number;
  keyword_match: number;
  experience_score: number;
  education_score: number;

  matched_skills: string[];
  missing_skills: string[];

  section_feedback: SectionFeedback;

  suggestions: string[];
  summary: string;
}