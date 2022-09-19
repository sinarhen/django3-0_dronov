from .models import Bb, Rubric
from django.shortcuts import render
from .forms import BbForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def index(request):
    bbs = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
    }
    return render(request, template_name="bboard/index.html", context=context)


def rubric_id(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs, 'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, template_name="bboard/by_rubric.html", context=context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(BbCreateView, self).get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
