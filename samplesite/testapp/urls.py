from django.urls import path
from .views import *

app_name = 'testapp'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('get/<path:filename>', get, name='get')
]

