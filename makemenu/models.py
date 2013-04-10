from django.db import models

# Create your models here.
class Dish(models.Model):

    dish_name = models.CharField(
        max_length= 255,
    )
    dish_weight = models.IntegerField(
        max_length= 10,
    )
    dish_price = models.FloatField(
        max_length=10,
    )

    def __str__(self):

        return ' '.join([
            self.dish_name,
            self.dish_weight,
            self.dish_price
            ])