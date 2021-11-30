from django.db import models

from django.conf import settings

class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='client',
                                on_delete=models.CASCADE,
                                primary_key=True)
    photo = models.ImageField(upload_to='media/%Y/%m/%d',
                              blank=True)

    SEX_TYPES = (
        ('M','Male'),
        ('F','Female'),
    )

    sex = models.CharField(max_length=1, 
                           choices=SEX_TYPES,
                           blank=True)

    def __str__(self):
        return self.user.username
