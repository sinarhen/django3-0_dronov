from django.db import models


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(verbose_name='Content', null=True, blank=True)
    price = models.FloatField(verbose_name='Price', null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, verbose_name='Published', db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rubric'
        verbose_name_plural = 'Rubrics'
        ordering = ['name']
