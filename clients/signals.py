from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from .models import Client

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_client_handler(sender, instance, created, **kwargs):
    if not created:
        return
    client = Client(user=instance,photo='no_image.png')
    client.save()
