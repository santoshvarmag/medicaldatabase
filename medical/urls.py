"""medical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers, views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from database import views
from database.views import CompanyNameViewSet


router = routers.DefaultRouter()
router.register("company", views.CompanyViewSet, basename="company")
router.register("company_bank", views.CompanyBankViewSet, basename="company_bank")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/gettoken/',TokenObtainPairView.as_view(), name='get_token'),
    path('api/refresh_token/',TokenRefreshView.as_view(), name='refresh_token'),
    path('api/company_by_name/<str:name>/', views.CompanyNameViewSet.as_view(), name='company_by_name')
]
