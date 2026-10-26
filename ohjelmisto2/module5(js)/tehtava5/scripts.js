"use strict";

const year = parseInt(prompt("Anna vuosiluku:"));

if (year % 400 === 0) {
    document.querySelector("#target").textContent = year + " on karkausvuosi.";
} else if (year % 100 === 0) {
    document.querySelector("#target").textContent = year + " ei ole karkausvuosi.";
} else if (year % 4 === 0) {
    document.querySelector("#target").textContent = year + " on karkausvuosi.";
} else {
    document.querySelector("#target").textContent = year + " ei ole karkausvuosi.";
}