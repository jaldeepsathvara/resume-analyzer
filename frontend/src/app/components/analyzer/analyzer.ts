import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AnalyzerService } from '../../services/analyzer'
import { ResumeAnalysis } from '../../models/analysis.model';

@Component({
  selector: 'app-analyzer',
  imports: [CommonModule, FormsModule],
  templateUrl: './analyzer.html',
  styleUrl: './analyzer.css',
  standalone: true,
})
export class Analyzer {
  selectedFile: File | null = null;
  uploadStatus: string = '';
  job_description: string = '';
  isUploading: boolean = false;
  isJD: boolean = false;
  pdfReady: boolean = false;
  result: ResumeAnalysis | null = null;

  constructor(
    private analyzerService: AnalyzerService,
    private cdr: ChangeDetectorRef
  ) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
    this.uploadStatus = '';
    this.pdfReady = false;
    this.result = null;
  }

  uploadPdf() {
    if (!this.selectedFile) {
      this.uploadStatus = 'Please upload a resume PDF.';
      return;
    }
    if (!this.job_description.trim()) {
      this.uploadStatus = 'Please enter a job description.';
      return;
    }
    const currentQuestion = this.job_description;
    // this.job_description = '';
    this.isJD = true;
    this.isUploading = true;
    this.analyzerService.analyzeResume(this.selectedFile, currentQuestion).subscribe({
      next: (res) => {
        this.uploadStatus = `✅ Upload successfully`;
        this.result = res;
        this.pdfReady = true;
        this.isUploading = false;
        this.cdr.detectChanges();
      },
      error: () => {
        this.uploadStatus = '❌ Upload failed.';
        this.isUploading = false;
        this.isJD = false;
        this.cdr.detectChanges();
      }
    });
  }
}
