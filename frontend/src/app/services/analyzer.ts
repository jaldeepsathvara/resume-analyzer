import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ResumeAnalysis } from '../models/analysis.model';

@Injectable({
  providedIn: 'root'
})
export class AnalyzerService {

  private apiUrl = 'http://localhost:8000/analyze/';

  constructor(private http: HttpClient) {}

  analyzeResume(file: File, jdText: string): Observable<ResumeAnalysis> {

    const formData = new FormData();

    formData.append('file', file);
    formData.append('jd_text', jdText);

    return this.http.post<ResumeAnalysis>(
      this.apiUrl,
      formData
    );
  }
}