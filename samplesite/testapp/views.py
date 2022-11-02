from django.shortcuts import render
from django.db import transaction


# Create your views here.


@transaction.non_atomic_requests
def my_view(request):
    return None


@transaction.atomic
def edit(request, pk):
    return None
