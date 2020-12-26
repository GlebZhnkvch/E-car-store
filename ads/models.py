from django.db import models
from django.utils import timezone
from brands.models import Brand, Year
from users.models import User
from django.core.validators import MinLengthValidator


class Ad(models.Model):
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)
    car_model = models.CharField(max_length=200)
    capacity = models.CharField(max_length=20, default='')
    year = models.ForeignKey(Year, related_name='year', on_delete=models.CASCADE)
    equipment = models.CharField(max_length=200)
    mileage = models.CharField(max_length=8)
    price = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    phone_number_ad = models.CharField(max_length=13, validators=[MinLengthValidator(12)])
    author_ad = models.CharField(max_length=20, default='')
    image = models.ImageField(upload_to="img", blank=False, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f"{self.car_model} ({self.author})"


def get_image_filename(instance, filename):
    pass
