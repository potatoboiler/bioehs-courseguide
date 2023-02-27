"""
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
from django.urls import path, include
from . import views, models
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/documentation/', views.site_documentation, name='site_documentation'),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='user_profile'),
    path('accounts/update/', views.edit_user, name='account_update'),
    path('accounts/alumni/', views.alumni, name='alumni_networking'),
    path('about/officers/', views.default, name='officers'),
    path('about/officers/<str:semester>/', views.officersBySemester, name='detail')
    ]
