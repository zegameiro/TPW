import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Author } from '../author';
import { AUTHORS } from '../authorslist';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-authors',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './authors.component.html',
  styleUrl: './authors.component.css'
})
export class AuthorsComponent {
  authors: Author[];
  selectedAuthor: Author | null = null;

  constructor() { 
    this.authors = AUTHORS;
  }

  onSelect(author: Author) :void {
    this.selectedAuthor = author;
  }
}

