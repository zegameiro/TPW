import { Mamal } from "./mamal";

export abstract class Feline extends Mamal {

    static nFelines: number;
    family: string;

    protected constructor(habitat: string, family: string) {
        super(habitat)
        Feline.nFelines++;
        this.family = family;
    }
} 