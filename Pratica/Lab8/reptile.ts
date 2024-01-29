export abstract class Reptile {

    static nReptile: number = 0;
    habitat: string

    protected constructor(habitat: string = "Earth") {
        this.habitat = habitat;
        Reptile.nReptile++;
    }

    show(): string {
        return `Ẁe are ${Reptile.nReptile} animals and my habitat is: ${this.habitat}`;
    }
}