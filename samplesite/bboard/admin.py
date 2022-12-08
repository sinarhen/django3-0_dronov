from django.contrib import admin
from .models import Bb, Rubric

# Register your models here.
admin.site.register(Bb)
admin.site.register(Rubric)


class BbAdmin(admin.ModelAdmin):
    list_display = ('title_and_rubric',
                    'content',
                    'price',
                    'published',
                    )

    def title_and_price(self):
        ...

    title_and_price.short
