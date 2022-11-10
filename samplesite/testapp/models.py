from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.validators import FileExtensionValidator


def get_path(instance, filename):
    return f'{instance.name}/{filename}'


class Image(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    image = models.FileField(upload_to=get_path, verbose_name='Image')
    desc = models.TextField(verbose_name='Description')


class Message(models.Model):
    ...

    class Meta:
        abstract = True


class PrivateMessage(Message):
    ...

    class Meta(Message.Meta):
        pass


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


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')


print(ContentType)
