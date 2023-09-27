"""
URL configuration for djangoProject project.

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
from internship.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:product_id>/', LessonByProductView.as_view(), name='lesson-by-product'),
    path('lessonshistory/<int:product_id>/', LessonAndHistoryByProductView.as_view(),
         name='lesson-and-history-by-product'),
    path('producthistory/', ProductStatisticsView.as_view(), name='product-list-statistic'),

]
