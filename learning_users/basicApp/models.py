from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    #Addition Fields
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __self__(self):
        return self.User.username