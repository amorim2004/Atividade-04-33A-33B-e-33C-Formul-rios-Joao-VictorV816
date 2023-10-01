"""django_project URL Configuration

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
from sitedoamorim import views

urlpatterns = [
    path('', views.meuApp,name='meuApp'),
    path('craque', views.create_craque),
    path('craque/update/<id>', views.update_craque),
    path('craque/delete/<id>', views.delete_craque),
    path('cont', views.create_cont),
    path('cont/update/<id>', views.update_cont),
    path('cont/delete/<id>', views.delete_cont),
    path('admin/', admin.site.urls),
]
