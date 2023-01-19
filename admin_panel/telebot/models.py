from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Clients(CreatedModel):
    telegram_id = models.BigIntegerField(
        verbose_name='Telegram ID пользователя',
        help_text='Telegram ID пользователя',
    )

    username = models.CharField(
        verbose_name='Username пользователя',
        help_text='Username пользователя',
        null=True,
        max_length=500
    )

    name = models.CharField(
        verbose_name='Имя пользователя',
        help_text='Имя пользователя',
        null=True,
        max_length=500
    )
