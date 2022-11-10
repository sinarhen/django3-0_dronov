from django.forms import formset_factory
from django.shortcuts import render
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


def index(request):
    pass

def add(request):
    pass

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
