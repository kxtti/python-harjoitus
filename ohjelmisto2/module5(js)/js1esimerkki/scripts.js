"use strict";
console.log("Hei maailma!");

document.querySelector("#target").innerHTML = "Testi!";

const age = prompt("Give your age:");

if (age < 18 && age >= 12){
    console.log("You're a minor");
} else if (age < 12){
    console.log("You're too young.");
    if (age < 5) {
        console.log("You're a toddler.");
    }
} else {
    console.log("You're an adult.");
}