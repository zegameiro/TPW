import { Cat } from "./cat";
import { Dog } from "./dog";

let cat = new Cat('Casa', 'Siamês', 'Barto');
let ct = cat.talk();
console.log(ct);

let dog = new Dog('Casa', 'Rafeiro');
let dt = dog.talk();
console.log(dt);

