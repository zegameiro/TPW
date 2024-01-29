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
exports.Canine = void 0;
var mamal_1 = require("./mamal");
var Canine = /** @class */ (function (_super) {
    __extends(Canine, _super);
    function Canine(habitat, race) {
        var _this = _super.call(this, habitat) || this;
        Canine.nCanines++;
        _this.race = race;
        return _this;
    }
    Canine.prototype.talk = function () {
        return _super.prototype.talk.call(this);
    };
    return Canine;
}(mamal_1.Mamal));
exports.Canine = Canine;
