from django.urls import path
from .import views

urlpatterns = [
    path('home',views.Home,name="home"),
    path('0-1year',views.ShopbyAgePage1,name="0-1year"),
    path('1-3year',views.ShopbyAgePage2,name="1-3year"),
    path('3+year',views.ShopbyAgePage3,name="3+year"),
    path('school',views.SchoolPage,name="school"),
    path('about',views.AboutusPage,name="about"),
    path('contect',views.ContectPage,name="contect"),
    path('register',views.RegisterPage,name="register"),
    path('login',views.LoginPage,name="login"),
    path('ulogin',views.Userlogin),
    path('logout',views.LogOut),
    path('register2',views.Register2),    
]

