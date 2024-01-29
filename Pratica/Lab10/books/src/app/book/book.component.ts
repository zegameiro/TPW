import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Book } from '../book';
import { BOOKS } from '../bookslist';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-book',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './book.component.html',
  styleUrl: './book.component.css'
})
export class BookComponent {
  books: Book[];
  selectedBook: Book | null = null;

  constructor() {
    this.books = BOOKS;
  }
  onSelect(book: Book) :void {
    this.selectedBook = book;
  }
}
