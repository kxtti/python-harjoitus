# Kierrätysseikkailu
# Elias Lauanne

# Pelin idea

Pelin ideana on, että pelaaja valitsee yhden kolmesta reitistä ja liikkuu valitun reitin eri paikkojen välillä etsien roskia.

Pelissä on Kotireitti, Kaupunkireitti ja Luontoreitti.

Reiteillä on eri vaikeustasot ja eri määrä roskia, jotka pelaajan täytyy kierrättää oikein läpäistäkseen pelin.

Jokaisella reitillä on kolme erilaista paikkaa ja paikoissa on omia roskia.

Oikein kierrätetystä roskasta saa yhden pisteen. Jos pelaaja lajittelee roskan väärin, peli päättyy.


# Pelin tavoite

Pelin tavoitteena on läpäistä pelaajan valitsema reitti kierrättämällä tarpeeksi roskia oikein.

Kotireitti on helppo ja sen läpäisemiseen tarvitaan 5 oikein kierrätettyä roskaa.

Kaupunkireitti on keskivaikea ja sen läpäisemiseen tarvitaan 10 oikein kierrätettyä roskaa.

Luontoreitti on vaikea ja sen läpäisemiseen tarvitaan 15 oikein kierrätettyä roskaa.


# Reitit ja vaikeustasot

Kotireitti - Helppo - 5 roskaa
- Keittiö
- Kylpyhuone
- Autotalli

Kaupunkireitti - Keskitaso - 10 roskaa
- Kauppa
- Koulu
- Bussipysäkki

Luontoreitti - Vaikea - 15 roskaa
- Metsä
- Ranta
- Retkeilyalue


# Miten peli liittyy kestävään kehitykseen

Peli liittyy YK:n kestävän kehityksen Agenda2030 tavoitteeseen 12, Vastuullista kuluttamista.

Erityisesti peli liittyy tavoitteeseen 12.5, jonka tavoitteena on vähentää jätteiden syntymistä ennaltaehkäisyn, kierrätyksen ja uudelleenkäytön avulla.

Pelissä pelaaja harjoittelee erilaisten jätteiden lajittelua ja kierrättämistä.


# Pelin toimintaperiaatteet

Ohjelman käynnistyessä peli kysyy pelaajalta nimen ja iän.

Jos pelaaja on alle 12-vuotias, peli sulkeutuu.

Muussa tapauksessa peli näyttää esittelytekstin ja peliohjeet erillisistä tekstitiedostoista.

Tämän jälkeen pelaaja valitsee yhden kolmesta reitistä ja samalla vaikeustason.

Jokaisella reitillä on kolme paikkaa. Pelaaja voi liikkua valitun reitin paikkojen välillä ja etsiä niistä roskia.

Eri paikoissa on erilaisia roskia.

Pelaaja voi tallentaa pelinsä tekstitiedostoon ja jatkaa tallennettua peliä myöhemmin samalla pelaajanimellä ja samalla reitillä.


# Pelin toiminnallisuudet

Etsi - etsii pelaajan nykyisestä sijainnista satunnaisen roskan. Pelaajan täytyy valita oikea jäteastia. Oikeasta vastauksesta saa yhden pisteen ja väärä vastaus päättää pelin.

Inventaario - näyttää kaikki tähän mennessä oikein kierrätetyt roskat.

Pisteet - näyttää pelaajan pisteiden määrän.

Liiku - näyttää valitun reitin sijainnit ja antaa pelaajan vaihtaa sijaintia.

Tallenna - tallentaa pelaajan nimen, reitin, sijainnin ja kierrätetyt roskat tekstitiedostoon.

Lopeta - lopettaa pelin.


# Pelin läpäiseminen

Pelin läpäisemiseen tarvittava pistemäärä riippuu valitusta reitistä.

Kotireitti vaatii 5 pistettä.

Kaupunkireitti vaatii 10 pistettä.

Luontoreitti vaatii 15 pistettä.

Kun pelaaja saavuttaa reitin tavoitteen, peli päättyy voittoon.


# Rakenne

Koodi on jaettu eri moduuleihin. Eri luokat ovat omissa moduuleissaan.

roska.py - sisältää Roska-luokan. Roskalla on nimi ja oikea jäteastia.

paikka.py - sisältää Paikka-luokan. Paikalla on nimi.

pelaaja.py - sisältää Pelaaja-luokan. Pelaajalla on nimi, kierrätetyt roskat ja nykyinen sijainti. Luokka sisältää myös pelaajan toimintoja hoitavat metodit.

peli.py - pelin pääohjelma. Se tuo muut luokat käyttöön ja sisältää muun muassa reitin valinnan, vaikeustasot, tallennuksen, latauksen ja pelin pääsilmukan.

intro.txt - sisältää pelin esittelytekstin.

ohjeet.txt - sisältää pelin ohjeet.