from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    images = models.ImageField(default='default_image.png', upload_to='profile_image', blank = True)


    def __str__(self):
        return f'{self.user.username} Profile'


# Method create images a 300x300 px
    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.images.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.images.path)
