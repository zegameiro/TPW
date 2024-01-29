import { Animal } from "./animal";

export abstract class Mamal extends Animal {

    static nMamals: number;
    protected constructor(habitat: string) {
        super(habitat)
        Mamal.nMamals++;
    }

    show(): string {
        return super.show() + `and mamals are ${Mamal.nMamals}`;
    }

    talk(): string {
        return `Talking: `;
    };
} 