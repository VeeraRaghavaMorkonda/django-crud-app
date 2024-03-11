from django.shortcuts import render
from django.shortcuts import render, redirect  
from .forms import MigrationTrackingForm  
from .models import MigrationTrackerModel  
import pandas as pd

# Create your views here.

def gcp_dashboard(request):    
    return render(request,"gcp_dashboard.html") 

def gcp_migraion_tracker(request):
    # Get all objects and convert to data list
        isit_apps_count = MigrationTrackerModel.objects.filter(pdo="Industrial Systems IT").count()
        isit_2024_apps_count = MigrationTrackerModel.objects.filter(pdo="Industrial Systems IT_2024").count()
        ford_credit_apps_count = MigrationTrackerModel.objects.filter(pdo="Ford Credit(FMCC)").count()
        ford_credit_2024_apps_count = MigrationTrackerModel.objects.filter(pdo="Ford Credit(FMCC)_2024").count()
        ford_pro_apps_count = MigrationTrackerModel.objects.filter(pdo="FORD PRO S").count()
        ierp_apps_count = MigrationTrackerModel.objects.filter(pdo="IERP").count()
        ierp_2024_apps_count = MigrationTrackerModel.objects.filter(pdo="iERP_2024").count()
        ito_apps_count = MigrationTrackerModel.objects.filter(pdo="ITO").count()
        ito_2024_apps_count = MigrationTrackerModel.objects.filter(pdo="ITO_2024").count()
        mss_apps_count = MigrationTrackerModel.objects.filter(pdo="MSS").count()  
        mss_2024_apps_count = MigrationTrackerModel.objects.filter(pdo="MSS_2024").count() 
        oceto_apps_count = MigrationTrackerModel.objects.filter(pdo="OCETO").count()
        oceto_2024_apps_count = MigrationTrackerModel.objects.filter(pdo="OCETO_2024").count()  
        staff_it_apps_count = MigrationTrackerModel.objects.filter(pdo="Staffs IT (Mexico)").count()             
        blanks_count = MigrationTrackerModel.objects.filter(pdo=None).count()
        total_count = MigrationTrackerModel.objects.count()

        data = {
            'isit_apps_count' : isit_apps_count,
            'isit_2024_apps_count' : isit_2024_apps_count,
            'ford_credit_apps_count' :ford_credit_apps_count,
            'ford_credit_2024_apps_count' : ford_credit_2024_apps_count,
            'ford_pro_apps_count' : ford_pro_apps_count,
            'ierp_apps_count' : ierp_apps_count,
            'ierp_2024_apps_count' : ierp_2024_apps_count,
            'ito_apps_count' : ito_apps_count,
            'ito_2024_apps_count' : ito_2024_apps_count,
            'mss_apps_count' : mss_apps_count,
            'mss_2024_apps_count' : mss_2024_apps_count,
            'oceto_apps_count' : oceto_apps_count,
            'oceto_2024_apps_count' : oceto_2024_apps_count,
            'staff_it_apps_count' : staff_it_apps_count,
            'blanks_count' : blanks_count,
            'total_count' : total_count

        }
        return render(request, 'gcp_migration_tracker.html', data)