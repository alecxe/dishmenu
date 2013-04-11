from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from makemenu.models import DishType

urlpatterns = patterns('',

    url(r'^$', makemenu.views.ListDishTypeView.as_view(),
        name='dishtypes-list', ),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=DishType,
            template_name='makemenu/dishes.html'),
            name='detail'),
    )