export abstract class Animal {
    static nAnimals: number = 0;
    habitat: string
    
    protected constructor(habitat: string = "Earth") {
        this.habitat = habitat;
        Animal.nAnimals++;
    }

    show(): string {
        return `Ẁe are ${Animal.nAnimals} animals and my habitat is: ${this.habitat}`;
    }
}