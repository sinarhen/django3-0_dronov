from .models import Bb, Rubric
from django.shortcuts import render
from .forms import BbForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import authenticate, login
import django.contrib.auth.views as dcav
from django.contrib.auth.forms import AuthenticationForm


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


class BbCreateView(UserPassesTestMixin, CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(BbCreateView, self).get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def test_func(self):
        return self.request.user.is_staff


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
