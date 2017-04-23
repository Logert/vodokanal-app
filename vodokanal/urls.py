"""vodokanal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import ListLics, detail_lics, ListDom, DetailDom, ListNasPunkt, DetailNasPunkt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ListLics.as_view(), name='index'),
    # lics
    url(r'^lics/$', ListLics.as_view(), name='list_lics'),
    url(r'^lics/(?P<lics_id>[0-9]+)/$', detail_lics, name='detail_lics'),
    # dom
    url(r'^dom/$', ListDom.as_view(), name='list_dom'),
    url(r'^dom/(?P<pk>[0-9]+)/$', DetailDom.as_view(), name='detail_dom'),
    # nas_punkt
    url(r'^nas_punkt/$', ListNasPunkt.as_view(), name='list_NasPunkt'),
    url(r'^nas_punkt/(?P<pk>[0-9]+)/$', DetailNasPunkt.as_view(), name='detail_NasPunkt'),


]
