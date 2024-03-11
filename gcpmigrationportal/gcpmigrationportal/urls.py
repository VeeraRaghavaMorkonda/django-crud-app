"""
URL configuration for gcpmigrationportal project.

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
from gcpservicemappings import views
from migrationtracker import views as tracker

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'), 
    path('gcp-dashboard', tracker.gcp_dashboard, name='gcp_dashboard'), 
    path('gcp-migration-tracker', tracker.gcp_migraion_tracker, name='gcp_migraion_tracker'),
    path('gcp-service-mappings', views.gcp_service_mappings, name='gcp_service_mappings'), 
    path('fordcredit-apps', views.fordcredit_apps, name='fordcredit_apps'), 
    path('fordcredit-service-observations', views.fordcredit_service_observations, name='fordcredit_service_observations'),
    path('total-apps', views.total_apps, name='total_apps'),  
    path('add-app',views.add_app, name='add_app'),  
    path('edit-app/<int:id>', views.edit_app, name='edit_app'),  
    path('update-app/<int:id>', views.update_app, name='update_app'),  
    path('delete-app/<int:id>', views.destroy_app, name='destroy_app'), 
]
