from django.forms import formset_factory

from .models import Bb, Rubric
from django.shortcuts import render
from .forms import BbForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import authenticate, login
import django.contrib.auth.views as dcav
from django.contrib.auth.forms import AuthenticationForm
from .forms import SearchForm


def formset_processing(request):
    fs = formset_factory(SearchForm, extra=3, can_order=True, can_delete=True)
    if request.method == 'POST':
        formset = fs(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data and not form.cleaned_data['DELETE']:
                    kw = form.cleaned_data['keyword']
                    rubric_id = form.cleaned_data['rubric'].pk
                    order = form.cleaned_data['ORDER']
                    #  Do any actions with cleaned data
            return render(request, 'bboard/process_result.html')
    else:
        formset = fs()
    context = {'formsets': formset}
    return render(request, 'bboard/formset.html', context)


def search(request):
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            kw = sf.cleaned_data["keyword"]
            rubric_id = sf.cleaned_data['rubric'].pk
            bbs = Bb.objects.filter(title__icontains=kw, rubric=rubric_id)
            return render(request, 'bboard/search.html', {'bbs': bbs})
    else:
        sf = SearchForm()
    return render(request, 'bboard/search.html', {'form': sf})


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

    # BbCreateView(UserPassesTestMixin, )
    # def test_func(self):
    #     return self.request.user.is_staff


# from django.contrib.auth.mixins import PermissionRequiredMixin
# class BbCreateView2(PermissionRequiredMixin, CreateView):
#     template_name = 'bboard/create.html'
#     form_class = BbForm
#     success_url = reverse_lazy('index')
#     permission_required = ('bboard.add_bb', 'bboard.change_bb', 'bboard.delete_bb')

class LoginClass(dcav.LoginView):
    template_name: str
    redirect_field_name: str  # Default "next"
    redirect_authenticated_user: str
    extra_context: dict  # Extra context to template
    success_url_allowed_hosts: list | set | tuple  # Default empty, allows redirecting to exact hosts
    authentication_form: AuthenticationForm  # Link to class of form login


class LogoutClass(dcav.LogoutView):
    next_page: str  # Page after logout
    template_name: str
    redirect_field_name: str  # Default "next"
    extra_context: dict  # Extra context to template
    success_url_allowed_hosts: list | set | tuple  # Default empty, allows redirecting to exact hosts


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


# Cookies
"""
def view(request):
  response = HttpResponse('blah')
  response.set_cookie('cookie_name', 'cookie_value')
"""

# Sessions

"""
if 'counter' in request.session:
    cnt = request.session['counter'] + 1
else: cnt = 1

request.session['counter'] = cnt
"""