# Vaatejemma
Tämän sovelluksen avulla voi helposti seurata, mitä lasten ulkovaatteita on käytettävissä esimerkiksi sisarukselta toiselle. Sovellus toimii varastokirjanpitäjänä.

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan vaatetietoa. Ilmoitukseen voi lisätä myös kuvia ja luokittelutietoa (vaatteen kunto ja onko kyseessä kesä-, vk- vai talvikauden vaate).
- Käyttäjä näkee kaikki sovellukseen lisätyt vaatetiedot. Vaatteita voi etsiä myös hakusanalla.
- Kaikkiin sovelluksessa oleviin ilmoituksiin voi lisätä kommentin.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät vaatteet ja tiedon vaatemäärästä.

## Sovelluksen asennus

Asenna flask-kirjasto:
```
$ pip install flask
``` 
Luo tietokannan taulut ja lisää alkutiedot:
```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```
Käynnistä sovellus:
```
$ flask run
```
