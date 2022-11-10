from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'testapp'

urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)