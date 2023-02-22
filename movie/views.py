from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from .forms import createform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
# Create your views here.

class MovieList(ListView):
    model = Movie
    # context_object_name = ''
    # template_name = 

class MovieDetail(DetailView):
    model = Movie
    # context_object_name =
    # template_name = 

def my_login(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect("movie_list")
        else:
            messages.info(request, 'username or password is incorrect')
                 
    context = {}
    return render(request, 'movie/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('log')

# @login_required(login_url='login')
def register(request):
    form = createform()

    if request.method =="POST":
        form = createform(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f"Hey! {name}, your account was successfully created")
            return redirect('log')

    context = {
        'form':form
    }
    return render(request, 'movie/register.html', context)
     