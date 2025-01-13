from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView  # וודא שזה מופיע
from .views import register_view

urlpatterns = [
    path('', views.guest_list, name='guest_list'),
    path('add/', views.add_guest, name='add_guest'),
    path('conditional/', views.conditional_redirect, name='conditional_redirect'),
    path('alternative/', views.alternative_page, name='alternative_page'),  # הדף
    path('video/', views.video_page, name='video_page'),
    path('questionnaire/', views.questionnaire_view, name='questionnaire'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]





