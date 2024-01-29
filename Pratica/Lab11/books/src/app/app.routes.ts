import { Routes } from '@angular/router';
import { AuthorsComponent } from './author/author.component';
import { TopComponent } from './top/top.component';

export const routes: Routes = [
    { path: 'authors', component: AuthorsComponent },
    { path: 'top', component: TopComponent },
];
