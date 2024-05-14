from django.contrib.auth.models import User
from django.db import models


class DishImage(models.Model):
    image = models.ImageField('Image:', upload_to='product_image/')


class Dish(models.Model):
    Choices_list = (
        ('done', 'Заказано'),
        ('none', 'Заказать'),
        ('delivering', 'Доставляеться'),
        ('cooking', 'Готовиться'),
        ('accepted', 'Принят'),
        ('none', 'none')
    )
    name = models.CharField('Name', max_length=30)
    info = models.TextField('Information')
    price = models.FloatField('Price')
    status = models.CharField(verbose_name='Status:', max_length=30, choices=Choices_list)
    images = models.ManyToManyField(DishImage, verbose_name='Images')
    quantity = models.IntegerField(verbose_name='Кол-во:', blank=True)


class Connect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank=True)

