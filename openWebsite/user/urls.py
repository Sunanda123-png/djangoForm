from . import views
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]