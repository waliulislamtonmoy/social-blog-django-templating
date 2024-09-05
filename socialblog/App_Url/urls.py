from django.urls import path,include

from App_Blog.views import HomeView
from App_Account.views import sign_in,sign_up,user_logout,Profile,user_change,password_change

urlpatterns = [
    path("",HomeView,name='home'),
    path("login/",sign_in,name="login"),
    path("register/",sign_up,name="register"),
    path("logout/",user_logout,name="logout"),
    path("profile/",Profile,name="profile"),
    path("change-profile/",user_change,name="change-profile"),
    path("password/",password_change,name="password_change")
    
]
