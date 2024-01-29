import { PUBLISHERS } from "./publisherslist";
import { AUTHORS } from "./authorslist";
import { Book } from "./book";

export const BOOKS: Book[]  = [
    {
        num: 1,
        title: 'Arquiteturas Distribuídas',
        date: new Date(2001, 3, 9),
        authors: [AUTHORS[0], AUTHORS[1]],
        publisher: PUBLISHERS[0]
    },
    {
        num: 2,
        title: 'Operação de Sistemas',
        date: new Date(2005, 6, 26),
        authors: [AUTHORS[2], AUTHORS[4]],
        publisher: PUBLISHERS[2]
    },
    {
        num: 3,
        title: 'Sistemas Físicos e de Multimédia',
        date: new Date(2010, 11, 19),
        authors: [AUTHORS[2]],
        publisher: PUBLISHERS[3]
    },
    {
        num: 4,
        title: 'Modelação e Análise de Sons',
        date: new Date(1995, 1, 30),
        authors: [AUTHORS[0], AUTHORS[1], AUTHORS[3], AUTHORS[4]],
        publisher: PUBLISHERS[4]
    },
    {
        num: 5,
        title: 'Segurança em Compiladores',
        date: new Date(2015, 7, 4),
        authors: [AUTHORS[2], AUTHORS[3]],
        publisher: PUBLISHERS[1]
    }
]