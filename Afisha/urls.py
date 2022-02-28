"""Afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_app import views
from  django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/',views.test),
    path('api/v1/name/',views.NAME_list_view),
    path('api/v1/name/<int:id>/',views.name_detail_view),
    path('api/v1/Movie/',views.Movie_list_view),
    path('api/v1/Movie/<int:id>/',views.MovieDetail),
    path('api/v1/Review/',views.Review_list_view),
    path('api/v1/Review/<int:id>/',views.R_detail_view),
    path('api/v1/Review/Movie',views.RSERA),
    path('api/v1/login/', views.authorization),
    path('api/v1/register/', views.registration),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]
