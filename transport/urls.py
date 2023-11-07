"""
URL configuration for transport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from adminapp import views
from adminapp.viewlogic import drivers
from adminapp.viewlogic import cleaners
from adminapp.viewlogic import login



urlpatterns = [
    path('admin/', admin.site.urls),
    # admin access

    path('api/register/supervisor', views.create_supervisor, name='create_supervisor'),
    path('api/supervisor/list', views.list_supervisor, name='list_supervisor'),

    # admin access end
    # admin and supervisor access

    path('api/driver/register', drivers.register_drivers, name='register_drivers'),
    path('api/driver/list', drivers.drivers_list, name='drivers_list'),
    path('api/cleaner/register', cleaners.register_cleaners, name='register_cleaners'),
    path('api/cleaners/list', cleaners.cleaners_list, name='cleaners_list'),

    # admin and supervisor access end
    
    # login
    path('api/login', login.login, name='login'),

    

]
