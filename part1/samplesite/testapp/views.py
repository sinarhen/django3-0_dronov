import os.path

from django.contrib import auth
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ImgUploadForm
from django.contrib.auth.models import User
from django.http import FileResponse
from samplesite.settings import BASE_DIR
from datetime import datetime

FILES_ROOT = os.path.join(BASE_DIR, 'files')


def output(request):
    imgs = []
    for entry in os.scandir(FILES_ROOT):
        imgs.append(os.path.basename(entry))
    context = {'imgs': imgs}
    return render(request, 'testapp/index.html', context)


def get(request, filename):
    fn = os.path.join(FILES_ROOT, filename)
    return FileResponse(open(fn, 'rb'), content_type='application/octet-stream')


def add(request):
    if request.method == 'POST':
        form = ImgUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            fn = f'{datetime.now().timestamp()}{os.path.splitext(uploaded_file)}'
            fn = os.path.join(FILES_ROOT, fn)
            with open(fn, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return redirect('testapp:index')
    form = ImgUploadForm()
    context = {'form': form}
    return render(request, 'testapp/index.html')


def index(request):
    if request.user.is_authenticated:
        form = ImgUploadForm()
        if request.method == 'POST':
            form = ImgUploadForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('testapp:index')
        """
        if form.is_valid():
            for file in request.FILES.getlist('img'):
                img = Image()
                img.desc = form.cleaned_data['desc']
                img.image = file
                img.save()
        """
        return render(request, template_name='testapp/index.html', context={'form': form})
    else:
        return redirect('testapp:login')


def login(request):
    fm = AuthenticationForm()
    if request.method == "POST":
        fm = AuthenticationForm(data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = auth.authenticate(username=uname, password=upass)
            auth.login(request, user)
            return redirect('testapp:index')
    err = fm.error_messages
    context = {'form': fm, 'err': err}
    return render(request, 'testapp/login.html', context)


# Create your views here.


@transaction.non_atomic_requests
def my_view(request):
    return None


@transaction.atomic
def edit(request, pk):
    return None


def manual_transaction_control(request):
    form = UserCreationForm()
    if form.is_valid():
        try:
            form.save()
            transaction.commit()
        except:
            transaction.rollback()


def manual_transaction_control_formset(request):
    formset = formset_factory(UserCreationForm, extra=2)()
    if formset.is_valid():
        for form in formset:
            if form.cleaned_data:
                sp = transaction.savepoint()
                try:
                    form.save()
                    transaction.savepoint_commit()
                except:
                    transaction.savepoint_rollback()
                transaction.commit()


def commit_handler():
    """some actions when transaction verified"""


transaction.on_commit(commit_handler)
