from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import reverse
from django.utils.text import slugify



class product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    shortDescription = models.CharField(max_length=360, default='empty')
    isActive = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse('product-details-page', args=[self.slug])

    def save(self, *args, **keyargs):
        self.slug = slugify(self.title)
        super().save(*args, **keyargs)

    def __str__(self):
        return f"{self.title} ({self.price})"
