from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.views.generic import FormView, ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Lics, Nas_punkt, Person, Dom, Kvartiry, Street, Lgoty, Tip_lgoty, \
    Pribory, MarkiPriborov


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
        paginator = Paginator(streets, 50)
        page = self.request.GET.get('page')
        try:
            streets = paginator.page(page)
        except PageNotAnInteger:
            streets = paginator.page(1)
        except EmptyPage:
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


# Типы льгот
class ListTipLgoty(ListView):
    model = Tip_lgoty
    success_url = '/tip_lgoty'
    template_name = 'main/tip_lgoty/tip_lgoty.html'


class DetailTipLgoty(DetailView):
    model = Tip_lgoty
    success_url = '/tip_lgoty'
    template_name = 'main/tip_lgoty/tip_lgoty_detail.html'


# Приборы учета
class ListPribory(ListView):
    model = Pribory
    success_url = '/pribory'
    template_name = 'main/pribory/pribory.html'


class DetailPribory(DetailView):
    model = Pribory
    success_url = '/pribory'
    template_name = 'main/pribory/pribory_detail.html'


# Марки приборов учета
class ListMarkiPribory(ListView):
    model = MarkiPriborov
    success_url = '/marki_pribory'
    template_name = 'main/marki_pribory/marki_pribory.html'


class DetailMarkiPribory(DetailView):
    model = MarkiPriborov
    success_url = '/marki_pribory'
    template_name = 'main/marki_pribory/marki_pribory_detail.html'