from django.db import models


class Snowboard(models.Model):
    class GenderChoices(models.TextChoices):
        FEMALE = 'Female'
        MALE = 'Male'
        UNISEX = 'Unisex'

    class TypeChoices(models.TextChoices):
        ROCKER = 'Rocker'
        CAMBER = 'Camber'

    class YearChoices(models.TextChoices):
        this_year = '2024'
        last_year = '2023'
        last_last_year = '2022'

    class StyleChoices(models.TextChoices):
        PARK = 'Park',
        FREE_RIDE = 'Free-ride'
        ALL_MOUNTAIN = 'All mountain'

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
    year = models.CharField(
        max_length=15,
        choices=YearChoices.choices,
        default=YearChoices.this_year
    )
    length_size = models.IntegerField(null=False)
    price_euro = models.FloatField(null=False)
    reference_link = models.CharField(max_length=700, null=True)
    true_twin = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.model_name
