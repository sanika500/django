from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('delete/<int:pk>',views.delete_g,name="delete"),
    path('edit/<int:pk>',views.edit_g,name="edit")


    # path('about',views.about,name="about"),
    # path('demo',views.demo,name="demo"),
    # path('hello',views.hello,name="hello"),


]