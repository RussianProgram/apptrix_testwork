from django.db import models
from django.conf import settings

class Client(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='client',
        on_delete=models.CASCADE,
        primary_key=True
    )
    photo = models.ImageField(
        upload_to='media/%Y/%m/%d',
        blank=True
    )


    SEX_TYPES = (
        ('M','Male'),
        ('F','Female'),
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_TYPES,
        blank=True)

    longitude = models.FloatField(
        verbose_name='Долгота',
        blank=True
    )
    latitude = models.FloatField(
        verbose_name='Широта',
        blank=True
    )


    def __str__(self):
        return f"{self.user.username}"


class Liked(models.Model):
    like_from = models.ForeignKey(
        'auth.User',
        related_name='like_from',
        on_delete=models.CASCADE
    )

    like_to = models.ForeignKey(
        'auth.User',
        related_name='like_to',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.like_from} like {self.like_to}'

