from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import LoginForm
from django.contrib.auth import authenticate, login
import sys
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['your_name']
            password = form.cleaned_data['password']
            # print(name, file=sys.stderr)
            # print(form['password'], file=sys.stderr)
            user = authenticate(username=name, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect('/home')
                print("Logged in", file=sys.stderr)
            else:
                args = {"form": form, 'name': name}
                messages.error(request, 'Wrong Password or email.')
                print("Not Logged in", file=sys.stderr)
                return render(request, 'login.html', args)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


class Login(TemplateView):
    def get(self, request, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required(login_url='/login')
def homepage(request):
    return render(request, 'homepage.html')
