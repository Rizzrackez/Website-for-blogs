from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    images = models.ImageField(default='default.jpg', upload_to='profile_image', blank = True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.pk})


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
