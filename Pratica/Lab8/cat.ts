import { Feline } from "./feline";

export class Cat extends Feline {
    
    static nCats: number;
    meow: string = "Meow";
    name: string;

    constructor(habitat: string, family: string, name: string, meow?: string) {
        super(habitat, family);
        this.name = name;
        Cat.nCats++;
        if(meow) {
            this.meow = meow;
        }
    }

    talk() {
        return super.talk() + `${this.meow}`;
    }
}