from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    USER = 'user', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'


class CustomUser(AbstractUser):
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='О себе'
    )
    role = models.CharField(
        max_length=500,
        choices=Role.choices,
        default=Role.USER,
        verbose_name='Уровень доступа (роль)'
    )
    confirmation_code = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Код подтверждения'
    )
    token = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Токен авторизации'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='e-mail пользователя'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.role == Role.ADMIN

    @property
    def is_moderator(self):
        return self.role == Role.MODERATOR
