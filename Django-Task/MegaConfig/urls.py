"""
URL configuration for MegaConfig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
import os
import glob
from .settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
]

for app in glob.glob(os.path.join(BASE_DIR, 'task_*')):
    if os.path.isdir(app):
        app_name = os.path.basename(app)
        urls_path = os.path.join(app, 'urls.py')
        if os.path.exists(urls_path):
            urlpatterns.append(path(f'{app_name}/', include(f'{app_name}.urls')))