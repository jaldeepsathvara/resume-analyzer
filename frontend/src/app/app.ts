import { Component, signal } from '@angular/core';
import { Analyzer } from '../app/components/analyzer/analyzer'
@Component({
  selector: 'app-root',
  imports: [Analyzer],
  templateUrl: './app.html',
  standalone: true
})
export class AppComponent {}
