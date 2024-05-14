from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.ListOfDishes.as_view(), name='dishes'),
    path('more/<int:pk>', views.DetailDish.as_view(), name='more'),
    path('logout', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
