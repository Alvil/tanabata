from django.db import models


class Wish(models.Model):
    wish = models.CharField(max_length=100)
    times_wished = models.IntegerField(default=1)
