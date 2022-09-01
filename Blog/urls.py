from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name="index"),
    path('blog', views.blog, name="blog"),
    path('<slug:slug>', views.blog_details, name="blog-details")
]
