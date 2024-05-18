from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.ListOfDishes, name='dishes'),
    path('more/<int:pk>', views.DetailDish, name='more'),
    path('logout', views.logout_view, name='logout'),
    path('/soda', views.ListOfDishesSoda, name='soda'),
    path('/alco', views.ListOfDishesAlco, name='alco'),
    path('/desert', views.ListOfDishesDesert, name='desert'),
    path('/first', views.ListOfDishesFirst, name='first'),
    path('/sec', views.ListOfDishesSec, name='sec'),
    path('/fast', views.ListOfDishesFast, name='fast'),
    path('/salat', views.ListOfDishesSalat, name='salat'),
    path('/tuck', views.ListOfDishesTuck, name='tuck'),
    path('corsina/', views.connect_to_corsina, name='corsina'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
