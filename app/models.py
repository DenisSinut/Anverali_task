from django.contrib.auth.models import AbstractUser
from django.db import models


type_choices = [('customer', "Заказчик"), ('customer', "Исполнитель")]


class User(AbstractUser):
    first_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name="Фамилия"
    )
    phone_number = models.CharField(
        max_length=11,
        blank=True,
        verbose_name="Номер телефона"
    )
    email = models.EmailField(
        unique=True,
        blank=True
    )
    type = models.CharField(
        blank=False,
        verbose_name="Тип",
        choices=type_choices,
        default="customer"
    )
    experience = models.TextField(
        blank=True,
        verbose_name="Опыт"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


    def __str__(self):
        return str(self.first_name)
