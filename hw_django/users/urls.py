from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # path("", views.main, name='root'),
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout')
]
