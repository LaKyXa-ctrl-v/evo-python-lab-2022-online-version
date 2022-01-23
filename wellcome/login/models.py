from django.db import models
from django.urls import reverse
# Create your models here.


class Person(models.Model):
    first_name = models.CharField(
        "Им'я", max_length=30, null=False)
    last_name = models.CharField(
        "Призвіще", max_length=30, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})

    class Meta:
        unique_together = [['first_name', 'last_name']]
