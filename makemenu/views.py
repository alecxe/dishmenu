# Create your views here.
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from makemenu.models import DishType, Dish
from django.http import HttpResponse

class ListDishTypeView(ListView):

    model = DishType
    template_name = 'makemenu\dishtypes_list.html'
    context_object_name='dishtypes_list'

class DetailDishTypeView(DetailView):

    model=DishType
    template_name='makemenu\dishes.html'



