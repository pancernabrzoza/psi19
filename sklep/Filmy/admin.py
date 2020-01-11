from django.contrib import admin
from .models import Film, Zamowienie, Klient, Magazyn, Pracownicy

admin.site.register(Film)
admin.site.register(Zamowienie)
admin.site.register(Klient)
admin.site.register(Magazyn)
admin.site.register(Pracownicy)
