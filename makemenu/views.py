# Create your views here.
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from makemenu.models import DishType, Dish
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render_to_response

class ListDishTypeView(ListView):

    model = DishType
    template_name = 'makemenu\dishtypes_list.html'
    context_object_name='dishtypes_list'

class DetailDishTypeView(DetailView):

    model=DishType
    template_name='makemenu\dishes.html'


def most_nourishing(request):
    #p = get_object_or_404(Poll, pk=poll_id)
    most_nourishing_dishes = {}
    for next_dish_type in DishType.objects.all():
        most_nourishing_dishes[next_dish_type.name] = next_dish_type.dish_set.aggregate(Max('dish_weight'))

    return render_to_response('makemenu/most_nourishing.html',most_nourishing_dishes)


