import { Canine } from "./canine";

export class Dog extends Canine {

    bark: string = "Oof Oof";
    static nDogs: number;

    constructor(habitat: string, race: string, bark?: string) {
        super(habitat, race);
        Dog.nDogs++;
        if (bark) 
            this.bark = bark

    }

    talk(){
        return super.talk() + `${this.bark}`;
    }

}
