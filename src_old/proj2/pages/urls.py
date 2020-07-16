from django.urls import path
from .views import home_view, contact_view, about_view, social_view, hello_there_view

urlpatterns = [
    path("", home_view, name="home"),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
    path("hello/<name>", hello_there_view, name="hello_there"),
]