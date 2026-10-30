const koirat = [];

for (let i = 0; i < 6; i++) {
  const nimi = prompt("Anna koiran nimi:");
  koirat.push(nimi);
}

koirat.sort();
koirat.reverse();

const lista = document.querySelector("#koiralista");

for (let i = 0; i < koirat.length; i++) {
  lista.innerHTML += "<li>" + koirat[i] + "</li>";
}