from django.db import models
from .validators import *


class RubricQuerySet(models.QuerySet):
    def order_by_bb_count(self):
        return self.annotate(cnt=models.Count('bb')).order_by('-cnt')


class RubricManager(models.Manager):
    """
    Add some methods to specialized fetching data from database
    """

    def get_queryset(self):
        return RubricQuerySet(self.model, using=self._db)

    def order_by_bb_count(self):
        return super(RubricManager, self).get_queryset().annotate(cnt=models.Count('bb')).order_by('cnt')

    def display_orders_count(self):
        query = super(RubricManager, self).get_queryset().annotate(cnt=models.Count('bb'))
        dct = {}
        for r in query:
            dct[r.name] = {'count': r.cnt, 'set': {r.bb_set.all()}}
        return dct


class Bb(models.Model):
    KINDS = ({
                 None: 'What are we doing?',
                 'a': 'Buying',
                 'b': 'Selling',
                 'c': 'Switching',
             }.items())
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(verbose_name='Content', null=True, blank=True)
    price = models.FloatField(verbose_name='Price', null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, verbose_name='Published', db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')
    kind = models.CharField(verbose_name='Kind', choices=KINDS, default='s', max_length=4)

    """Validation on field level"""

    def clean(self):
        errors = {}
        if self.content and len(self.content) < 40:
            errors['content'] = ValidationError('At least 40 symbols')
        elif self.price and self.price <= 100:
            errors['price'] = ValidationError('Price should be at least 100')
        if errors:
            """
            errors = {
                    'content': ValidationError('At least 40 symbols),
                    'price': ValidationError('Price should be at least 100'),
                }
            """
            raise ValidationError(errors)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Name')
    objects = models.Manager()
    bbs = RubricManager()  # bbs1, bbs2 = RubricQuerySet.as_manager(), models.Manager.from_queryset(RubricQuerySet)()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rubric'
        verbose_name_plural = 'Rubrics'
        ordering = ['name']


class RevRubric(Rubric):
    """
    proxy = True allows use Rubric objects in database
    (database inherits)
    """

    class Meta:
        ordering = ['-name']
        proxy = True
