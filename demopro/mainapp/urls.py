from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    # path('about',views.about,name="about"),
    # path('demo',views.demo,name="demo"),
    # path('hello',views.hello,name="hello"),


]