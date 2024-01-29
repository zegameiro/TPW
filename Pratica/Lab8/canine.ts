import { Mamal } from "./mamal";

export abstract class Canine extends Mamal {

    static nCanines: number;
    race: string;

    protected constructor(habitat: string, race: string) {
        super(habitat)
        Canine.nCanines++;
        this.race = race;
    }

    talk() {
        return super.talk();
    }
} 