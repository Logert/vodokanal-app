from django.shortcuts import render, get_object_or_404, redirect
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


class DetailLics(LicsMixin, DetailView):
    template_name = 'main/lics/lics_detail.html'


class UpdateLics(LicsMixin, UpdateView):
    fields = ['kod_dom', 'kod_kvart', 'tel', 'prim', 'email']
    template_name = 'main/lics/lics_update.html'


class DeleteLics(LicsMixin, DeleteView):
    template_name = 'main/lics/lics_delete.html'