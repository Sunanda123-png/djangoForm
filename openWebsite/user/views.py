from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import SignInForm,SignUpForm
from .models import User

import json
import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'sign-in.html', {'form': form})


@csrf_exempt
def signup(request):
    """
    this method is created for user registration
    :param request: passing the request
    :return: outcome result
    """

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = json.loads(request.body)
            user_name = data.get("user_name")
            name = data.get("name")
            password = data.get("password")
            email = data.get("email")
            user = User(user_name=user_name, name=name, password=password, email=email)
            user.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'sign-up.html', {'form': form})

