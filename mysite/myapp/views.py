from multiprocessing import context

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render



@login_required
def index(request):
    return render(request, 'myapp/etusivu.html')

@login_required
def lainaus(request):
    return render(request, 'borrowing/lainaus.html')

@login_required
def palautus(request):
    return render(request, 'return/palautus.html')

@login_required
def uusituote(request):
    return render(request, 'newproduct/uusituote.html')

@login_required
def tuotelista(request):
    return render(request, 'productlist/tuotelista.html')

@login_required
def lainantarkistus(request):
    return render(request, 'borrowingcheck/lainantarkistus.html')

@login_required
def eipaasyoikeutta(request):
    return render(request, 'noaccess/eipaasyoikeutta.html')

@login_required
def yllapito_etusivu(request):
    return render(request, 'maintenance/yllapito_etusivu.html')

@login_required
def yllapito_korjaalaina(request):
    return render(request, 'maintenance/yllapito_korjaalaina.html')

@login_required
def yllapito_korjaatuote(request):
    return render(request, 'maintenance/yllapito_korjaatuote.html')

@login_required
def yllapito_poistatuote(request):
    return render(request, 'maintenance/yllapito_poistatuote.html')
