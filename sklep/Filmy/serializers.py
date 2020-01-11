from rest_framework import serializers
from .models import Film, Zamowienie, Klient, Magazyn, Pracownicy


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

    # nazwa = serializers.CharField(required=True)
    # autor = serializers.CharField(required=True)
    # cena = serializers.IntegerField(required=True)
    # data_premiery = serializers.DateField(required=True)

    def create(self, validated_data):
        return Film.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.autor = validated_data.get('autor', instance.autor)
        instance.cena = validated_data.get('cena', instance.cena)
        instance.data_premiery = validated_data.get('data_premiery', instance.data_premiery)
        instance.save()
        return instance


class ZamowienieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields = '__all__'

    # film = serializers.CharField(required=True)
    # klient = serializers.CharField(required=True)
    # ilosc = serializers.IntegerField(required=True)
    # data_zwrotu = serializers.DateField(required=True)
    # data_wypozyczenia = serializers.CharField(required=True)

    def create(self, validated_data):
        return Zamowienie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.film = validated_data.get('film', instance.film)
        instance.klient = validated_data.get('klient', instance.klient)
        instance.ilosc = validated_data.get('ilosc', instance.ilosc)
        instance.data_zwrotu = validated_data.get('data_zwrotu', instance.data_zwrotu)
        instance.data_wypozyczenia = validated_data.get('data_wypozyczenia', instance.data_wypozyczenia)
        instance.save()
        return instance


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'

    # imie = serializers.CharField(required=True)
    # nazwisko = serializers.CharField(required=True)
    # pesel = serializers.IntegerField(required=True)
    # znizka = serializers.IntegerField(required=True)
    # nr_telefonu = serializers.IntegerField(required=True)
    # adress = serializers.CharField(required=True)

    def create(self, validated_data):
        return Klient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.pesel = validated_data.get('pesel', instance.pesel)
        instance.znizka = validated_data.get('znizka', instance.znizka)
        instance.nr_telefonu = validated_data.get('nr_telefonu', instance.nr_telefonu)
        instance.adress = validated_data.get('adress', instance.adress)
        instance.save()
        return instance


class MagazynSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazyn
        fields = '__all__'

    # nazwa_filmu = serializers.CharField(required=True)
    # ilosc = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Magazyn.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa_filmu = validated_data.get('nazwa_filmu', instance.nazwa_filmu)
        instance.ilosc = validated_data.get('ilosc', instance.ilosc)
        instance.save()
        return instance


class PracownicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownicy
        fields = '__all__'

    # imie = serializers.CharField(required=True)
    # nazwisko = serializers.CharField(required=True)
    # pesel = serializers.IntegerField(required=True)
    # znizka = serializers.IntegerField(required=True)
    # nr_telefonu = serializers.IntegerField(required=True)
    # adress = serializers.CharField(required=True)
    # stanowisko = serializers.CharField(required=True)
    # wyplata = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Pracownicy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.pesel = validated_data.get('pesel', instance.pesel)
        instance.znizka = validated_data.get('znizka', instance.znizka)
        instance.nr_telefonu = validated_data.get('nr_telefonu', instance.nr_telefonu)
        instance.adress = validated_data.get('adress', instance.adress)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.wyplata = validated_data.get('wyplata', instance.wyplata)
        instance.save()
        return instance