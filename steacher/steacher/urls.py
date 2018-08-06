"""steacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from steacher.views import hello
from steacher.views import about
from steacher.views import writers
from steacher.views import current_datetime
from steacher.views import hours_ahead

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('about_us/', about),
    path('about_us/ParisaDaj/', writers),
    path('about_us/DonyaSharafoddin/', writers),
    path('main/', current_datetime),
    path('main/plus/<offset>/', hours_ahead),
]
