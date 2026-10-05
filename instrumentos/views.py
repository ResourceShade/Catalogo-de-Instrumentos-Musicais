from django.shortcuts import render, get_object_or_404
from .models import Instrumento


def index(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'index.html', {'instrumentos': instrumentos})


def detalhe(request, id):
    instrumento = get_object_or_404(Instrumento, id=id)
    return render(request, 'detalhe.html', {'instrumento': instrumento})
