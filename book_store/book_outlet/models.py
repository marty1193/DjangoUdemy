from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)


class Aurthor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE,null=True)


    def full_name(self):
        return (f"{self.first_name} {self.last_name}")

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    aurthor = models.ForeignKey(Aurthor, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} ({self.rating})'
