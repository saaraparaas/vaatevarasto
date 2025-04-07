# Lastenvaatteiden varasto

Tehty:
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään ja muokkaamaan vaatetietoa.
- Käyttäjä näkee sovellukseen lisätyt vaatetiedot.

Tulossa:
- Käyttäjä pystyy poistamaan vaatetietoa.
- Käyttäjä pystyy etsimään vaatetietoa hakusanalla.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät vaatetiedot.
- Käyttäjä pystyy valitsemaan vaatetiedolle yhden tai useamman luokittelun (esimerkiksi talvivaatteet/vk-vaatteet/kesävaatteet, kokoluokka, kunto).
- Käyttäjä pystyy lisäämään kommentin vaatetietoon.

# Sovelluksen asennus

Asenna flask-kirjasto:

$ pip install flask

Luo tietokannan taulut ja lisää alkutiedot:

$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql

Käynnistä sovellus näin:

$ flask run
