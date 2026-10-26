"use strict";

const num1 = parseInt(prompt("Anna ensimmäinen kokonaisluku:"));
const num2 = parseInt(prompt("Anna toinen kokonaisluku:"));
const num3 = parseInt(prompt("Anna kolmas kokonaisluku:"));

const summa = num1 + num2 + num3;
const tulo = num1 * num2 * num3;
const keskiarvo = summa / 3;

document.querySelector("#target").innerHTML =
    "Summa: " + summa + "<br>" +
    "Tulo: " + tulo + "<br>" +
    "Keskiarvo: " + keskiarvo;