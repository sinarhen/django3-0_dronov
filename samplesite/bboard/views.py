from .models import Bb
from django.shortcuts import render


def index(request):
    bbs = Bb.objects.order_by('-published')
    context = {
        'bbs': bbs
    }
    return render(request, template_name="index.html", context=context)