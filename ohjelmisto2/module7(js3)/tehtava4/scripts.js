const luvut = [];

let luku = Number(prompt("Anna luku (0 lopettaa):"));

while (luku !== 0) {
  luvut.push(luku);
  luku = Number(prompt("Anna luku (0 lopettaa):"));
}

luvut.sort((a, b) => b - a);

for (let i = 0; i < luvut.length; i++) {
  console.log(luvut[i]);
}