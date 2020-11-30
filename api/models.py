from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.CharField(max_length=200)
    active = models.BooleanField(default=True, blank = True, null = True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email