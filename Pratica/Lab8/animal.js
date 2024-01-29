"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Animal = void 0;
var Animal = /** @class */ (function () {
    function Animal(habitat) {
        if (habitat === void 0) { habitat = "Earth"; }
        this.habitat = habitat;
        Animal.nAnimals++;
    }
    Animal.prototype.show = function () {
        return "\u1E80e are ".concat(Animal.nAnimals, " animals and my habitat is: ").concat(this.habitat);
    };
    Animal.nAnimals = 0;
    return Animal;
}());
exports.Animal = Animal;
