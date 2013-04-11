from django.db import models

# Create your models here.
class DishType(models.Model):

    name = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return self.name

class Dish(models.Model):

    dishType = models.ForeignKey(DishType)
    dish_name = models.CharField(
        max_length=255,
    )
    dish_weight = models.IntegerField(
        default=0,
    )
    dish_price = models.FloatField(
        default=0,
    )

    def __str__(self):

        return ' '.join([
            self.dish_name,
            self.dish_weight,
            self.dish_price
            ])

    def __unicode__(self):
        return self.dish_name