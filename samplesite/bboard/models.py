from django.db import models


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name='Content', null=True)
    price = models.FloatField(verbose_name='Price', null=True)
    published = models.DateTimeField(auto_now_add=True, verbose_name='Published')

