from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Index, Main, Price_list

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/', Main.as_view(), name='main'),
    path('pricelist/', Price_list.as_view(), name='pricelist')
]
