# Create your views here.
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse
from makemenu.models import DishType

class ListContactView(ListView):

    model = DishType
    template_name = 'makemenu\dishtypes_list.html'