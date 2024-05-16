from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django_recaptcha.fields import ReCaptchaField
from .forms import UserCreation
from django.views.generic import ListView, DetailView
from .models import Dish, Connect


def user_login(request):
    captcha = ReCaptchaField()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'register/login.html', {'captcha': captcha})


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
    return render(request, 'restaurant/main.html', {'model': model})


def ListOfDishesSoda(request):
    model = Dish.objects.filter(type='soda')
    return render(request, 'restaurant/main.html', {'model': model})


class DetailDish(DetailView):
    model = Dish
    template_name = 'restaurant/more_dish.html'
    context_object_name = 'dish'


def connect_to_corsina(request):
    cors = Connect.objects.filter(user=request.user)
    return render(request,'restaurant/corsina.html', {'cors': cors})