from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    title = models.CharField('Название', max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Родительская ветка',
        related_name='subthreads'
    )
    content = models.TextField('Содержание')
    created_at = models.DateTimeField('Создание', auto_now_add=True)
    updated_at = models.DateTimeField('Обновление', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ветка'
        verbose_name_plural = 'Ветки'


class Comment(models.Model):
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Тред'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    content = models.TextField('Текст комментария')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.author.username} к "{self.thread.title}"'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
