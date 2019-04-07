from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_do_list, name='to_do_list'),
]