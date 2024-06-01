from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django_recaptcha.fields import ReCaptchaField
from .forms import UserCreation, LoginForm, PaymentForm, ConnectForm
from .models import Dish, Connect, DishImage


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password1'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Ошибка в имени или парол')
    else:
        form = LoginForm()
    return render(request, 'register/login.html', {'form': form})


def user_login_l(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password1'])
            if user is not None:
                login(request, user)
                return redirect('dishes-l')
            else:
                form.add_error(None, 'Ошибка в имени или парол')
    else:
        form = LoginForm()
    return render(request, 'register/login-l.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreation()
    return render(request, 'register/registrate.html', {'form': form})


def register_l(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login-l')
    else:
        form = UserCreation()
    return render(request, 'register/registrate-l.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def logout_view_l(request):
    logout(request)
    return redirect('dishes-l')


def ListOfDishes(request):
    dishes = Dish.objects.all().prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesLight(request):
    dishes = Dish.objects.all().prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesSoda(request):
    dishes = Dish.objects.filter(kind='soda').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesSalat(request):
    dishes = Dish.objects.filter(kind='salat').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesTuck(request):
    dishes = Dish.objects.filter(kind='tuck').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesFast(request):
    dishes = Dish.objects.filter(kind='fast').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesSec(request):
    dishes = Dish.objects.filter(kind='sec').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})



def ListOfDishesDesert(request):
    dishes = Dish.objects.filter(kind='desert').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesAlco(request):
    dishes = Dish.objects.filter(kind='alco').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesFirst(request):
    dishes = Dish.objects.filter(kind='first').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesSoda_l(request):
    dishes = Dish.objects.filter(kind='soda').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesSalat_l(request):
    dishes = Dish.objects.filter(kind='salat').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesTuck_l(request):
    dishes = Dish.objects.filter(kind='tuck').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesFast_l(request):
    dishes = Dish.objects.filter(kind='fast').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesSec_l(request):
    dishes = Dish.objects.filter(kind='sec').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})



def ListOfDishesDesert_l(request):
    dishes = Dish.objects.filter(kind='desert').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesAlco_l(request):
    dishes = Dish.objects.filter(kind='alco').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})


def ListOfDishesFirst_l(request):
    dishes = Dish.objects.filter(kind='first').prefetch_related('dishimage_set')
    dishes_with_images = [
        (dish, dish.dishimage_set.first().image.url if dish.dishimage_set.exists() else None)
        for dish in dishes
    ]
    return render(request, 'restaurant/main-light.html', {'dishes_with_images': dishes_with_images})


@login_required(login_url='login')
def DetailDish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    model = DishImage.objects.filter(dishes=dish)
    if request.method == 'POST':
        form = ConnectForm(request.POST)
        if form.is_valid():
            con = form.save()
            con.user = request.user
            con.dish = dish
            con.save()
    else:
        form = ConnectForm(request.POST)
    return render(request, 'restaurant/more_dish.html', context={'dish': dish, 'images': model, 'form': form})


@login_required(login_url='login-l')
def DetailDish_l(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    model = DishImage.objects.filter(dishes=dish)
    if request.method == 'POST':
        form = ConnectForm(request.POST)
        if form.is_valid():
            con = form.save(commit=False)
            con.user = request.user
            con.dish = dish
            con.save()
    else:
        form = ConnectForm(request.POST)
    return render(request, 'restaurant/more_dish-l.html', context={'dish': dish, 'images': model, 'form': form})


@login_required(login_url='login')
def connect_to_corsina(request):
    cors = Connect.objects.filter(user=request.user)
    return render(request,'restaurant/corsina.html', {'cors': cors})


@login_required(login_url='login-l')
def connect_to_corsina_l(request):
    cors = Connect.objects.filter(user=request.user)
    return render(request,'restaurant/corsina-l.html', {'cors': cors})


@login_required(login_url='login')
def pay(request, pk):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save()
            payment.user = request.user
            payment.save()
            dish = get_object_or_404(Dish, pk=pk)
            Connect.objects.create(user=request.user, dish=dish)
            return redirect('success')
    else:
        form = PaymentForm()

    return render(request, 'restaurant/payment.html', {'form': form})


@login_required(login_url='login-l')
def pay_l(request, pk):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save()
            payment.user = request.user
            payment.save()
            dish = get_object_or_404(Dish, pk=pk)
            Connect.objects.create(user=request.user, dish=dish)
            return redirect('success')
    else:
        form = PaymentForm()

    return render(request, 'restaurant/payment-l.html', {'form': form})


def success(requests):
    return render(requests, 'restaurant/success.html')


def success_l(requests):
    return render(requests, 'restaurant/success-l.html')
