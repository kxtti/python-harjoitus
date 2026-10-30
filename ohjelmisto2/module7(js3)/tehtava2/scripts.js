const osallistujat = [];

const maara = Number(prompt("Anna osallistujien lukumäärä:"));

for (let i = 0; i < maara; i++) {
  const nimi = prompt("Anna osallistujan nimi:");
  osallistujat.push(nimi);
}

osallistujat.sort();

document.write("<ol>");

for (let i = 0; i < osallistujat.length; i++) {
  document.write("<li>" + osallistujat[i] + "</li>");
}

document.write("</ol>");