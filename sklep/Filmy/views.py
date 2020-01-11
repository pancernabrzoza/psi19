from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import generics

# Create your views here.


class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class ZamowienieList(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer


class ZamowienieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class MagazynList(generics.ListCreateAPIView):
    queryset = Magazyn.objects.all()
    serializer_class = MagazynSerializer


class MagazynDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazyn.objects.all()
    serializer_class = MagazynSerializer


class PracownicyList(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer


class PracownicyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
