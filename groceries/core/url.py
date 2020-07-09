from django.urls import path

from core import views

urlpatterns = [
    path('', views.front_page),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signin/front/', views.front),
    path('signin/front/edit/', views.edit)
]
