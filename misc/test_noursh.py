from django.core.management import setup_environ
from dishmenu import settings

setup_environ(settings)

from makemenu.models import DishType, Dish
from django.db.models import Max

print DishType.objects.values('dishtype_id').annotate(Max('dish_weight'))


