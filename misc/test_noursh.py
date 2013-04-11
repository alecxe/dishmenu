from django.core.management import setup_environ
from dishmenu import settings

setup_environ(settings)

from makemenu.models import DishType, Dish
from django.db.models import Max

most_nourishing_dishes = {}
for next_dish_type in DishType.objects.all():
    most_nourishing_dishes[next_dish_type.name] = next_dish_type.dish_set.aggregate(Max('dish_weight'))

print most_nourishing_dishes
