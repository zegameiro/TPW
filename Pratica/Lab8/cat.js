"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.Cat = void 0;
var feline_1 = require("./feline");
var Cat = /** @class */ (function (_super) {
    __extends(Cat, _super);
    function Cat(habitat, family, name, meow) {
        var _this = _super.call(this, habitat, family) || this;
        _this.meow = "Meow";
        _this.name = name;
        Cat.nCats++;
        if (meow) {
            _this.meow = meow;
        }
        return _this;
    }
    Cat.prototype.talk = function () {
        return _super.prototype.talk.call(this) + "".concat(this.meow);
    };
    return Cat;
}(feline_1.Feline));
exports.Cat = Cat;
