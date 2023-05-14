from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('second/', views.Second),
    path('third/', views.third)
]
