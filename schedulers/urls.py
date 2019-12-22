from django.urls import path

from . import views

urlpatterns = [
    path('user/register', views.RegisterView.as_view(), name='register_views'),

]