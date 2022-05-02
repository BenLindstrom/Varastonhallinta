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


