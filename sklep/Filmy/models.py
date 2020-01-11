from django.db import models


class Film(models.Model):
    nazwa = models.CharField(max_length=50)
    autor = models.CharField(max_length=20)
    cena = models.IntegerField()
    data_premiery = models.DateField()

    def __str__(self):
        return self.cena + ", " + self.nazwa


class Zamowienie(models.Model):
    film = models.CharField(max_length=50)
    klient = models.CharField(max_length=200)
    ilosc = models.IntegerField()
    data_zwrotu = models.DateField()
    data_wypozyczenia = models.DateField()

    def __str__(self):
        return self.klient + ", " + self.film + ", " + self.data_zwrotu


class Klient(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    pesel = models.IntegerField()
    znizka = models.IntegerField()
    nr_telefonu = models.IntegerField()
    adress= models.CharField(max_length=200)

    def __str__(self):
        return self.imie + ", " + self.nazwisko + ", " + self.nr_telefonu


class Magazyn(models.Model):
    nazwa_filmu = models.CharField(max_length=50)
    ilosc = models.IntegerField()
    def __str__(self):
        return self.nazwa_filmu + ", " + self.ilosc


class Pracownicy(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    pesel = models.CharField(max_length=11)
    znizka = models.IntegerField()
    nr_telefonu = models.IntegerField()
    adress = models.CharField(max_length=200)
    stanowisko = models.CharField(max_length=200)
    wyplata = models.FloatField()

    def __str__(self):
        return self.imie + ", " + self.nazwisko + ", " + self.stanowisko

# Create your models here.
