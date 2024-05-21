from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django_recaptcha.fields import ReCaptchaField
from .forms import UserCreation, LoginForm
from .models import Dish, Connect, DishImage


def user_login(request):
    # captcha = ReCaptchaField()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password1=cd['password1'])
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm(request.POST)
    return render(request, 'register/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            Connect.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreation()
    return render(request, 'register/registrate.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def ListOfDishes(request):
    model = Dish.objects.all()
    model1 = DishImage.objects.all()
    return render(request, 'restaurant/main.html', {'model': model, 'model1': model1[::3]})


def ListOfDishesSoda(request):
    model = Dish.objects.filter(kind='soda')
    return render(request, 'restaurant/main.html', {'model': model})


def ListOfDishesSalat(request):
    model = Dish.objects.filter(kind='salat')
    return render(request, 'restaurant/main.html', {'model': model})


def ListOfDishesTuck(request):
    model = Dish.objects.filter(kind='tuck')
    return render(request, 'restaurant/main.html', {'model': model})


def ListOfDishesFast(request):
    model = Dish.objects.filter(kind='fast')
    return render(request, 'restaurant/main.html', {'model': model})


def ListOfDishesSec(request):
    model = Dish.objects.filter(kind='sec')
    return render(request, 'restaurant/main.html', {'model': model})



def ListOfDishesDesert(request):
    model = Dish.objects.filter(kind='desert')
    return render(request, 'restaurant/main.html', {'model': model})


def ListOfDishesAlco(request):
    model = Dish.objects.filter(kind='alco')
    return render(request, 'restaurant/main.html', {'model': model})


def ListOfDishesFirst(request):
    model = Dish.objects.filter(kind='first')
    model1 = DishImage.objects.all()
    return render(request, 'restaurant/main.html', {'model': model, 'model1': model1[1:3]})


@login_required(login_url='login')
def DetailDish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    model = DishImage.objects.filter(dishes=dish)
    return render(request, 'restaurant/more_dish.html', context={'dish': dish, 'images': model})


@login_required(login_url='login')
def connect_to_corsina(request):
    cors = Connect.objects.filter(user=request.user)
    return render(request,'restaurant/corsina.html', {'cors': cors})


@login_required(login_url='login')
def connect_create(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    Connect.objects.create(user=request.user, dish=dish)
    return redirect('/')
