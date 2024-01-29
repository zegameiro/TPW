import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Publisher } from '../publisher';
import { PUBLISHERS } from '../publisherslist';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-publisher',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './publisher.component.html',
  styleUrl: './publisher.component.css'
})
export class PublisherComponent {
  publishers: Publisher[];
  selectedPublisher: Publisher | null = null;

  constructor() {
    this.publishers = PUBLISHERS;
  }

  onSelect(publisher: Publisher) :void {
    this.selectedPublisher = publisher;
  }
}
