from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lainaus/', views.lainaus, name='lainaus'),
    path('palautus/', views.palautus, name='palautus'),
    path('uusituote/', views.uusituote, name='uusituote'),
    path('tuotelista/', views.tuotelista, name='tuotelista'),
    path('lainantarkistus/', views.lainantarkistus, name='lainantarkistus'),
    path('eipaasyoikeutta/', views.eipaasyoikeutta, name='eipaasyoikeutta'),
    path('yllapito/', views.yllapito_etusivu, name='yllapito_etusivu'),
    path('yllapito/korjaalaina/', views.yllapito_korjaalaina, name='yllapito_korjaalaina'),
    path('yllapito/korjaatuote/', views.yllapito_korjaatuote, name='yllapito_korjaatuote'),
    path('yllapito/poistatuote/', views.yllapito_poistatuote, name='yllapito_poistatuote'),
]