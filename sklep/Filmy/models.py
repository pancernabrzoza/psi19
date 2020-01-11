from django.db import models


class Film(models.Model):
    nazwa = models.CharField(max_length=50)
    rezyser = models.CharField(max_length=20)
    cena = models.IntegerField()
    data_premiery = models.DateField()


class Klient(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    pesel = models.IntegerField()
    znizka = models.IntegerField()
    nr_telefonu = models.IntegerField()
    adress= models.CharField(max_length=200)


class Magazyn(models.Model):
    nazwa_filmu = models.CharField(max_length=50)
    ilosc = models.IntegerField()


class Pracownicy(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    pesel = models.CharField(max_length=11)
    znizka = models.IntegerField()
    nr_telefonu = models.IntegerField()
    adress = models.CharField(max_length=200)
    stanowisko = models.CharField(max_length=200)
    wyplata = models.FloatField()


class Zamowienie(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    data_zwrotu = models.DateField()
    data_wypozyczenia = models.DateField()

# Create your models here.
