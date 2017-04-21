from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView
from .models import Lics, Nas_punkt


class ListLics(ListView):
    model = Lics
    template_name = 'main/lics.html'


class CreateLics(CreateView):
    model = Lics
    fields = ['kod_dom', 'kod_kvart', 'tel', 'prim', 'email']
    success_url = '/listlics'
