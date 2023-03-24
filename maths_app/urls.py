from django import views
from django.urls import path


from django.urls import path
from . import views
urlpatterns = [
    path('',views.my_app, name='mathsApp')
]
