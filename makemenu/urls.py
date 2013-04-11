from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from makemenu.models import DishType
import makemenu.views

urlpatterns = patterns('',

    url(r'^$', makemenu.views.ListDishTypeView.as_view(),
        name='dishtypes-list', ),
    url(r'^(?P<pk>\d+)/$',makemenu.views.DetailDishTypeView.as_view(),
        name='dishes', ),
    )