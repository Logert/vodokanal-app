from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.views.generic import FormView, ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Lics, Nas_punkt, Person, Dom, Kvartiry, Street, Lgoty, Tip_lgoty


# Лицевые счета
class ListLics(ListView):
    model = Lics
    success_url = '/lics'
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


# Дома
class ListDom(ListView):
    model = Dom
    success_url = '/dom'
    template_name = 'main/dom/dom.html'


class DetailDom(DetailView):
    model = Dom
    success_url = '/dom'
    template_name = 'main/dom/dom_detail.html'


# Населенные пункты
class ListNasPunkt(ListView):
    model = Nas_punkt
    success_url = '/nas_punkt'
    template_name = 'main/nas_punkt/nas_punkt.html'


class DetailNasPunkt(DetailView):
    model = Nas_punkt
    success_url = '/nas_punkt'
    template_name = 'main/nas_punkt/nas_punkt_detail.html'


# Физ лица
class ListPersons(ListView):
    model = Person
    success_url = '/persons'
    template_name = 'main/persons/persons.html'


class DetailPersons(DetailView):
    model = Person
    success_url = '/persons'
    template_name = 'main/persons/persons_detail.html'


# Квартиры
class ListKvartiry(ListView):
    model = Kvartiry
    success_url = '/kvartiry'
    template_name = 'main/kvartiry/kvartiry.html'


class DetailKvartiry(DetailView):
    model = Kvartiry
    success_url = '/kvartiry'
    template_name = 'main/kvartiry/kvartiry_detail.html'


# Улицы
class ListStreets(ListView):
    model = Street
    success_url = '/streets'
    template_name = 'main/streets/streets.html'

    def get_queryset(self):
        streets = Street.objects.all()
        # Отбираем первые 50 улиц
        paginator = Paginator(streets, 50)
        page = self.request.GET.get('page')
        try:
            streets = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            streets = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            streets = paginator.page(paginator.num_pages)
        return streets


class DetailStreets(DetailView):
    model = Street
    success_url = '/streets'
    template_name = 'main/streets/streets_detail.html'


# Льготы
class ListLgoty(ListView):
    model = Lgoty
    success_url = '/lgoty'
    template_name = 'main/lgoty/lgoty.html'


class DetailLgoty(DetailView):
    model = Lgoty
    success_url = '/lgoty'
    template_name = 'main/lgoty/lgoty_detail.html'