# Lastenvaatteiden varasto

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan vaatetietoa.
- Käyttäjä näkee sovellukseen lisätyt vaatetiedot.
- Käyttäjä pystyy etsimään vaatetietoa hakusanalla.

Tulossa:
- Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät vaatetiedot.
- Käyttäjä pystyy valitsemaan vaatetiedolle yhden tai useamman luokittelun (esimerkiksi talvivaatteet/vk-vaatteet/kesävaatteet, kokoluokka, kunto).
- Käyttäjä pystyy lisäämään kommentin vaatetietoon.

# Sovelluksen asennus

Asenna flask-kirjasto:
- $ pip install flask

Luo tietokannan taulut ja lisää alkutiedot:
- $ sqlite3 database.db < schema.sql
- $ sqlite3 database.db < init.sql

Käynnistä sovellus:
- $ flask run
