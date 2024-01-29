import { Injectable } from '@angular/core';
import { Author } from '../author';

@Injectable({
  providedIn: 'root'
})
export class AuthorService {
  private baseURL = "http://localhost:8000/ws/"
  constructor() { }

  async getAuthor(id: number): Promise<Author> {
    const url :string = this.baseURL + "author?id=" + id;
    const data :Response = await fetch(url);
    return await data.json() ?? undefined;
  }

  async getAuthors(): Promise<Author[]> {
    const url :string = this.baseURL + "author";
    const data :Response = await fetch(url);
    return await data.json() ?? [];
  }

  async getAuthorsN(num: number): Promise<Author[]> {
    const url :string = this.baseURL + "author?num=" + num;
    const data :Response = await fetch(url);
    return await data.json() ?? [];
  }

  async createAuthor(au: Author): Promise<any> {
    const url :string = this.baseURL + 'authorcre';
    const data :Response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(au)
    });
    return data.json();
  }

  async updateAuthor(au: Author): Promise<any> {
    const url :string = this.baseURL + 'authorupd';
    const data :Response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(au)
    });
    return data.json();
  }

  async deleteAuthor(au: Author): Promise<any> {
    const url :string = this.baseURL + 'authordel/' + au.id;
    const data :Response = await fetch(url, {
      method: 'DELETE',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(au)
    });
    return data.text();
  }
}
