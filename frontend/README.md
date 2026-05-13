# Resume Analyzer Frontend

Angular frontend for the **AI Resume Analyzer** project.

This application allows users to upload a resume PDF, paste a job description, and view an AI-generated resume analysis including match score, keyword match, matched skills, missing skills, section-wise feedback, suggestions, and summary.

## Features

- Upload resume PDF
- Paste job description
- Send resume and job description to FastAPI backend
- Display ATS-style analysis result
- Show match score and keyword match score
- Display matched and missing skills
- Show section-wise feedback
- Clean and responsive UI

## Tech Stack

- Angular
- TypeScript
- HTML
- CSS
- RxJS
- FastAPI backend integration

## Project Structure

```text
src/app/
├── components/
│   └── analyzer/
│       ├── analyzer.component.ts
│       ├── analyzer.component.html
│       └── analyzer.component.css
├── services/
│   └── analyzer.service.ts
├── models/
│   └── analysis.model.ts
├── app.component.ts
├── app.component.html
└── app.config.ts