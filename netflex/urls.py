from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('single_movie/<int:movie_id>',views.single_movie,name="single_movie")
]
