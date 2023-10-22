from django.db import models


class Snowboard(models.Model):
    class GenderChoices(models.TextChoices):
        FEMALE = 'F', 'Female'
        MALE = 'M', 'Male'
        UNISEX = 'U', 'Unisex'

    class TypeChoices(models.TextChoices):
        ROCKER = 'R', 'Rocker'
        CAMBER = 'C', 'Camber'

    class StyleChoices(models.TextChoices):
        PARK = 'P', 'Park',
        FREE_RIDE = 'F', 'Free-ride'
        ALL_MOUNTAIN = 'A', 'All mountain'

    model_name = models.CharField(max_length=200, null=False)
    style = models.CharField(
        max_length=15,
        choices=StyleChoices.choices,
        default=StyleChoices.ALL_MOUNTAIN
    )
    type = models.CharField(
        max_length=15,
        choices=TypeChoices.choices,
        default=TypeChoices.CAMBER
    )
    gender = models.CharField(
        max_length=15,
        choices=GenderChoices.choices,
        default=GenderChoices.UNISEX
    )
    length_size = models.IntegerField(null=False)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.model_name
