from django.shortcuts import render

from lections.models import Specialization, Lection

def index(request):
    context = {
        'title': 'OpenLection',
    }
    return render(request,'lections/index.html', context)

def lections(request):
    context = {
        'title': 'OpenLection - Ашық сабақ',
        'lections': Lection.objects.all(),
        'specializations': Specialization.objects.all(),
    }
    return render(request,'lections/lections.html', context)
