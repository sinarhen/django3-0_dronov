from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', rubric_id, name='rubric_select'),
    path('search/', search, name='search')
]
