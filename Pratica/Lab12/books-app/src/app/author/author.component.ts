import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Author } from '../../author';
import { AUTHORS } from '../../authorslist';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-author',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './author.component.html',
  styleUrl: './author.component.css'
})
export class AuthorComponent {
  authors: Author[];
  selectedAuthor: Author | null = null;

  constructor() { 
    this.authors = AUTHORS;
  }

  onSelect(author: Author) :void {
    this.selectedAuthor = author;
  }
}
