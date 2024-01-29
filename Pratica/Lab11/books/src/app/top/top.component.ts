import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Author } from '../author';
import { AUTHORS } from '../authorslist';

@Component({
  selector: 'app-top',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './top.component.html',
  styleUrl: './top.component.css'
})
export class TopComponent {
  authors: Author[];

  constructor() { 
    this.authors = AUTHORS.slice(0, 3);
  }
}
