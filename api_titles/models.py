from datetime import date

from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Категория',
                            db_index=True)
    slug = models.SlugField(max_length=20,
                            unique=True,
                            db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Жанр',
                            db_index=True)
    slug = models.SlugField(max_length=20,
                            unique=True,
                            db_index=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование',
        db_index=True
    )
    year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Год выпуска',
        validators=(MaxValueValidator(date.today().year),),
        db_index=True
    )
    description = models.TextField(blank=True, verbose_name='Описание')
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('-id',)

    def __str__(self):
        return self.name
