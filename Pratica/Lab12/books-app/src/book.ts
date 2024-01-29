import { Author } from "./author";
import { Publisher } from "./publisher";

export interface Book {
    num: number,
    title: string;
    date: Date;
    authors: Author[];
    publisher: Publisher;
}