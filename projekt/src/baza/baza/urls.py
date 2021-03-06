"""baza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from strony import views
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('start', views.Start, name='home'),
    path('StronaGlowna', views.StronaGlowna, name='home_page'),
    path('Weryfikacja', views.Weryfikacja, name='weryfikacja'),
    path('Wyloguj', views.wyloguj, name='wyloguj'),
    path('zakladanie_konta/', views.zakladanie_konta, name='Zalkadanie_konta'),
    path('Statystyki', views.Statystyki, name='statystyki'),
    path('Roczniki', views.Roczniki, name='roczniki'),
    path('Regulamin', views.Regulamin, name='regulamin'),
    path('Kontakt', views.Kontakt, name='kontakt'),
    path('rocznik/<int:lata>/', views.rocznik, name='latapodstrony'),
    path('glosowanie/<str:id>/', views.glosowanie, name="Glosowanie"),
    path('Wyniki/<str:id>/', views.Wyniki_glosowania, name="Wyniki_glosowania"),
    path('blad/', views.blad, name="Blad"),

]
