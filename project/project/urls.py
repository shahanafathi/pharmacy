"""
URL configuration for project project.

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
from app import views
from django.conf import settings
from django.conf .urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('Login',views.Login,name='Login'),
    path('logout', views.logout, name='logout'),
    #####user
    path('user_register',views.user_register,name='user_register'),
    path('user_home',views.user_home,name='user_home'),
    path('search',views.search,name='search'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),

    ###Epharmacyuser
    path('pharm_register',views.pharm_register,name='pharm_register'),
    path('pharm_profile',views.pharm_profile,name='pharm_profile'),
    path('edit_pharm',views.edit_pharm,name='edit_pharm'),
    path('pharm_home',views.pharm_home,name='pharm_home'),
    path('add_medicine', views.add_medicine, name='add_medicine'),
    # path('medicine_view', views.medicine_view, name='medicine_view'),
    path('edit_medicine/<int:id>', views.edit_medicine, name='edit_medicine'),
    path('medicine_view', views.medicine_view, name='medicine_view'),
    path('delete_med/<int:id>',views.delete_med,name='delete_med'),
]


if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)