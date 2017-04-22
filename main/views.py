from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.views.generic import FormView, ListView, DetailView
from .models import Lics, Nas_punkt, Person

# Лицевые счета


class ListLics(ListView):
    model = Lics
    success_url = '/listlics'
    template_name = 'main/lics/lics.html'


def detail_lics(request, lics_id):
    lics = Lics.objects.get(lics=lics_id)
    try:
        person = Person.objects.filter(lics=lics_id)
    except Person.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'main/lics/lics_detail.html',
                  {'lics': lics,
                   'persons': person})
