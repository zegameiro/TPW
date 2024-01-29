import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Author } from '../../author';
import { AUTHORS } from '../../authorslist';
import { AuthorService } from '../author.service';

@Component({
  selector: 'app-top',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './top.component.html',
  styleUrl: './top.component.css'
})
export class TopComponent {
  authors: Author[] = [];
  authorService: AuthorService = inject(AuthorService);

  constructor() { 
    this.authorService.getAuthorsN(4).then((auths: Author[]) :void => {
      this.authors = auths;
    })
  }
}
