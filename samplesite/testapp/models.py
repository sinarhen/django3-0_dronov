from django.db import models

# Create your models here.
class Spare(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)


class Machine(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    spares = models.ManyToManyField(Spare,
                                    through='Kit',
                                    through_fields=('machine', 'spare'))


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField()
