from django.db import models


class Room(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, default='')
    detail = models.CharField(max_length=50, default='')
    image = models.CharField(max_length=30, default='home.jpg')

    class Meta:
        ordering = ['created']
