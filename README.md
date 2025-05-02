# Lastenvaatteiden varasto
Tämän sovelluksen avulla voi helposti seurata, mitä lasten ulkovaatteita on käytettävissä esimerkiksi sisarukselta toiselle. Sovellus toimii varastokirjanpitäjänä.

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan vaatetietoa.
- Käyttäjä näkee sovellukseen lisätyt vaatetiedot.
- Käyttäjä pystyy etsimään vaatetietoa hakusanalla.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät vaatetiedot.
- Käyttäjä pystyy valitsemaan vaatetiedolle kaksi eri luokittelua (minkä kauden vaate ja vaatteen kunto).
- Käyttäjä pystyy lisäämään kuvan vaatetietoon.
- Käyttäjä pystyy lisäämään kommentin vaatetietoon.

Tulossa:
- Sovelluksen käyttäjäsivut näyttävät tilastoja.

# Sovelluksen asennus

Asenna flask-kirjasto:
- $ pip install flask

Luo tietokannan taulut ja lisää alkutiedot:
- $ sqlite3 database.db < schema.sql
- $ sqlite3 database.db < init.sql

Käynnistä sovellus:
- $ flask run
