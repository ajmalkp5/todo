"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/all/',views.Todotypelistview.as_view(),name="todo-list"),
    path('todo/add/',views.todocreateview.as_view(),name='todo-add'),
    path('todo/<int:pk>/',views.Tododetailview.as_view(),name='todo-detail'),
    path('todo/<int:pk>/remove/',views.Tododeleteview.as_view(),name='todo-delete'),
    path('todo/<int:pk>/edit/',views.Todoupdateview.as_view(),name="todo-update"),
    path('register/',views.SignupView.as_view(),name="todo-register"),
    path('signin/',views.Signinview.as_view(),name="signin"),
    path('signout/',views.Signout.as_view(),name="signout")
    


]
