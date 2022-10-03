from django import views
from django.urls import path
from  .  views import  login_api, get_user_data,register_api

urlpatterns = [
    path('login/',views.login_api),
    path('user/', views.get_user_data),
    path('register/', register_api.as_view()),
]
