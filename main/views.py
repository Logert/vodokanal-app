from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView, DeleteView
from .models import Lics, Nas_punkt, Person

# Лицевые счета
class LicsMixin(object):
    model = Lics
    success_url = '/listlics'


class ListLics(LicsMixin, ListView):
    template_name = 'main/lics/lics.html'


class CreateLics(LicsMixin, CreateView):
    fields = ['kod_dom', 'kod_kvart', 'tel', 'prim', 'email']
    template_name = 'main/lics/lics_create.html'


def detail_lics(request, lics_id):
    lics = Lics.objects.get(lics=lics_id)
    try:
        person = Person.objects.filter(lics=lics_id)
    except Person.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'main/lics/lics_detail.html',
                  {'lics': lics,
                   'persons': person})


class UpdateLics(LicsMixin, UpdateView):
    fields = ['kod_dom', 'kod_kvart', 'tel', 'prim', 'email']
    template_name = 'main/lics/lics_update.html'


class DeleteLics(LicsMixin, DeleteView):
    template_name = 'main/lics/lics_delete.html'