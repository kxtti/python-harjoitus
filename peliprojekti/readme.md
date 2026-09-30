# Kierrätysseikkailu
# Elias Lauanne

# Pelin idea
Pelin ideana on, että pelaaja liikkuu eri paikkojen välillä ja etsii roskia. Löydetyt roskat täytyy tottakai kierrättää, ja oikein kierrätetystä roskasta saa aina pisteen. Jos pelaaja lajittelee roskan väärin, peli päättyy.
Lajittelumahdollisuuksia on lasi-, muovi-, metalli-, paperi-, elektroniikka, bio- ja pahvijäte

# Pelin tavoite
Pelin tavoitteena on kierrättää mahdollisimman paljon roskia eri paikoissa. Oikeista kierrätyksistä saa pisteen, ja koko ajan pitää olla tarkkana, koska jos pelaaja arvaa väärin peli päättyy.

# Miten liittyy kestävään kehitykseen
Peli liittyy ainakin YK:n kestävän kehityksen Agenda2030 tavoitteeseen 12. Vastuullista kuluttamista, ja etenkin sen ala-aiheeseen 12.5: Vähentää vuoteen 2030 mennessä merkittävästi jätteiden syntymistä ennaltaehkäisyn, kierrätyksen ja uudelleenkäytön keinoin.

# Pelin toimintaperiaatteet
Ohjelman käynnistyessä se kysyy pelaajalta nimen ja iän. Mikäli pelaaja on alle 12-vuotias, peli sulkeutuu. Muussa tapauksessa peli toivottaa pelaajan tervetulleeksi ja tulostaa päävalikon. Päävalikossa on kaikki oleellinen ja pelaaja antaa komentoja kunnes kirjoittaa "lopeta", jolloin peli sulkeutuu.

# Pelin toiminnallisuudet
etsi - etsii satunnaisen roskan, jonka jälkeen peli kysyy mihin se kuuluu lajitella. Pelaajan täytyy tietää mihin jätteeseen roska kuuluu ja kirjoittaa se. Oikeasta vastauksesta saa yhden pisteen, ja väärästä vastauksesta peli päättyy.

# Rakenne
Koodi on jaettu eri moduuleihin. Eri luokat ovat omissa moduuleissaan.
roska.py - Roska: roskan nimi ja sitä vastaava oikea roska
paikka.py - Paikka: paikan nimi
pelaaja.py - Pelaaja: pelaajan nimi, kierrätetyt roskat, sijainti sekä pelin toimintoja hoitavat metodit.
peli.py pääohjelma "main program": importtaa luokat käyttöön ja pyörittää peliä.