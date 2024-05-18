from django.contrib.auth.models import User
from django.db import models


class Dish(models.Model):
    Choices_list = (
        ('done', 'Заказано'),
        ('none', 'Заказать'),
        ('delivering', 'Доставляеться'),
        ('cooking', 'Готовиться'),
        ('accepted', 'Принят')
    )
    Type_list = (
        ('soda', 'Напитки'),
        ('desert', 'Десерты'),
        ('first', 'Первое'),
        ('salat', 'Салаты'),
        ('sec', 'Второе'),
        ("fast", "Фаст-фуд"),
        ("alco", "Алкоголь"),
        ("tuck", "Закуски"),
    )
    name = models.CharField('Name', max_length=30)
    info = models.TextField('Information')
    price = models.FloatField('Price')
    status = models.CharField(verbose_name='Status:', max_length=30, choices=Choices_list)
    quantity = models.IntegerField(verbose_name='Кол-во:', blank=True, null=True)
    kind = models.CharField(verbose_name='Type:', max_length=30, choices=Type_list)


class DishImage(models.Model):
    image = models.ImageField('Image:', upload_to='product_image/')
    dishes = models.ManyToManyField(Dish, verbose_name='Dishes:')


class Connect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank=True, null=True)

