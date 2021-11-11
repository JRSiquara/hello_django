"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views

if views.opcao == 'H':
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<int:idade>/', views.hello)
    ]
elif views.opcao == 'S':
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('soma/<int:num1>/<int:num2>/', views.soma)
    ]
elif views.opcao == 'M':
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('multi/<int:num1>/<int:num2>/', views.multi)
    ]
elif views.opcao == 'D':
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('divisao/<int:num1>/<int:num2>/', views.divisao)
    ]
elif views.opcao == 'U':
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('subtracao/<int:num1>/<int:num2>/', views.subtracao)
    ]
