from django.contrib import admin
from accounts.models import UserProfile
from django.db import models


admin.site.site_header = 'MySite'

admin.site.register(UserProfile)