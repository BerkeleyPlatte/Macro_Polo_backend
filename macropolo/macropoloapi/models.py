from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    pass
    weight = models.IntegerField(default=0)
    fat_factor = models.IntegerField(default=0.2)
    carb_factor = models.IntegerField(default=1)
    protein_factor = models.IntegerField(default=1.2)
    sodium_factor = models.IntegerField(default=12)
    fiber_factor = models.IntegerField(default=0.2)

    def __str__(self):
        return self.username


class Food(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    fat = models.IntegerField(default=0)
    carb = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("Food")
        verbose_name_plural = ("Foods")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Food_detail", kwargs={"pk": self.pk})
