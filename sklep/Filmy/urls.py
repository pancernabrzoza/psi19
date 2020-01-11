from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    path(r'^api-auth/', include('rest_framework.urls')),

    path('filmy/',views.FilmList.as_view()),

    path('zamowienie/',views.ZamowienieList.as_view()),

    path('klient/', views.KlientList.as_view()),

    path('magazyn/', views.MagazynList.as_view()),

    path('pracownicy/', views.PracownicyList.as_view()),
}

urlpatterns=format_suffix_patterns(urlpatterns)