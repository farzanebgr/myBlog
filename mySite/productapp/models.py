
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    shortDescription = models.CharField(max_length=360, default='empty')
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.price})"
