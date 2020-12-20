from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api_titles.models import Title
from api_users.models import CustomUser


class Review(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Наименование'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )
    score = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1),
                    MaxValueValidator(10))
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)

    def __str__(self):
        if len(self.text) > 30:
            return f'{self.text[:30]}...'
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='authors',
        verbose_name='Автор'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзывы'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        if len(self.text) > 30:
            return f'{self.text[:30]}...'
        return self.text
