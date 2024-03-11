from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect  
from gcpservicemappings.forms import ServiceMappingForm  
from gcpservicemappings.models import ServiceMappingModel  
import pandas as pd
 
# Create your views here. 

# Utility Functions

def convert_to_dataframe(objects):
    # Create an empty list to store data dictionaries
    data_list = []

    # Iterate through the queryset and create dictionaries for each object
    for obj in objects:
        data_dict = {
            # Add key-value pairs for each field you want in the DataFrame
                'app_id': obj.app_id,    
                'app_name': obj.app_name, 
                'pdo': obj.pdo,
                'sla': obj.sla, 
                'cia': obj.cia,
                'current_state_tech_stack': obj.current_state_tech_stack,
                'future_state_tech_stack': obj.future_state_tech_stack,
                'migration_roadmap': obj.migration_roadmap, 
                'current_state_db': obj.current_state_db,    
                'in_scope': obj.in_scope, 
                'architecture_type': obj.architecture_type, 
                'external_load_balancer': obj.external_load_balancer, 
                'internal_load_balancer': obj.internal_load_balancer, 
                'apigee': obj.apigee,
                'cloud_armor': obj.cloud_armor,
                'cloud_dns': obj.cloud_dns,
                'cloud_run': obj.cloud_run, 
                'gcp_caas': obj.gcp_caas, 
                'onprem_caas': obj.onprem_caas,   
                'compute_engine': obj.compute_engine,
                'cloud_function': obj.cloud_function,
                'cloud_storage': obj.cloud_storage,
                'pub_sub': obj.pub_sub,
                'cloudsql_mssql_se': obj.cloudsql_mssql_se,
                'cloudsql_mssql_ee': obj.cloudsql_mssql_ee,
                'cloudsql_pg': obj.cloudsql_pg,
                'onprem_db': obj.onprem_db,
                'big_query': obj.big_query,
                'cloud_scheduler': obj.cloud_scheduler,
                'memory_store': obj.memory_store,
                'cloud_monitoring': obj.cloud_monitoring,
                'cloud_logging': obj.cloud_logging,
                'secret_manager': obj.secret_manager,
                'fire_store': obj.fire_store,
                'data_flow': obj.data_flow,
                'mongo_db_atlas': obj.mongo_db_atlas,
                'cloud_build': obj.cloud_build,
                'adfs': obj.adfs,
                'azure_ad': obj.azure_ad,
                'no_of_cloud_run_ms': obj.no_of_cloud_run_ms,
                'deployment_topology': obj.deployment_topology,
                'deployment_topology_tobedeleted': obj.deployment_topology_tobedeleted,
                'availability': obj.availability,
                'downtime': obj.downtime,
                'remarks': obj.remarks,
                'comparision_notes': obj.comparision_notes,
                'verification': obj.verification,
                'business_value': obj.business_value,
                'business_remarks': obj.business_remarks,
                'planned_launch_date': obj.planned_launch_date,
                'devsecops_pipeline': obj.devsecops_pipeline,
                'app_pipeline': obj.app_pipeline,
                'iac_pipeline': obj.iac_pipeline,   
                'fossa': obj.fossa,
                'checkmarx': obj.checkmarx,
                'cycode': obj.cycode,
                'sonarqube': obj.sonarqube,   
                'crunch_42': obj.crunch_42,
                'automated_testing_before_deploy': obj.automated_testing_before_deploy,
                'automated_testing_after_deploy': obj.automated_testing_after_deploy,
                'monitoring': obj.monitoring,
                'sre': obj.sre,
                'deviation': obj.deviation,
                'target_db': obj.target_db,
                'migration_scope': obj.migration_scope,
                'migration_category': obj.migration_category,
            # ... add more fields as needed
        }
        data_list.append(data_dict)

    # Create the DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    return df

def landing_page(request):
    return render(request, 'landing.html')



def gcp_service_mappings(request):
      # Get all objects and convert to data list
        isit_apps_count = ServiceMappingModel.objects.filter(pdo="Industrial Systems IT").count()
        isit_2024_apps_count = ServiceMappingModel.objects.filter(pdo="Industrial Systems IT_2024").count()
        ford_credit_apps_count = ServiceMappingModel.objects.filter(pdo="Ford Credit(FMCC)").count()
        ford_credit_2024_apps_count = ServiceMappingModel.objects.filter(pdo="Ford Credit(FMCC)_2024").count()
        ford_pro_apps_count = ServiceMappingModel.objects.filter(pdo="FORD PRO S").count()
        ierp_apps_count = ServiceMappingModel.objects.filter(pdo="IERP").count()
        ierp_2024_apps_count = ServiceMappingModel.objects.filter(pdo="iERP_2024").count()
        ito_apps_count = ServiceMappingModel.objects.filter(pdo="ITO").count()
        ito_2024_apps_count = ServiceMappingModel.objects.filter(pdo="ITO_2024").count()
        mss_apps_count = ServiceMappingModel.objects.filter(pdo="MSS").count()  
        mss_2024_apps_count = ServiceMappingModel.objects.filter(pdo="MSS_2024").count() 
        oceto_apps_count = ServiceMappingModel.objects.filter(pdo="OCETO").count()
        oceto_2024_apps_count = ServiceMappingModel.objects.filter(pdo="OCETO_2024").count()  
        staff_it_apps_count = ServiceMappingModel.objects.filter(pdo="Staffs IT (Mexico)").count()             
        blanks_count = ServiceMappingModel.objects.filter(pdo=None).count()
        total_count = ServiceMappingModel.objects.count()

        fordcredit = ServiceMappingModel.objects.filter(pdo="Ford Credit(FMCC)")
        df = convert_to_dataframe(fordcredit)
        count = df[(df['adfs'].isnull()) & (df['azure_ad'].isnull())].shape[0]

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
            'total_count' : total_count,
            'count':count

        }
        
        return render(request, 'servicemappings.html', data)


def fordcredit_apps(request):
    fordcreditapps = ServiceMappingModel.objects.filter(pdo="Ford Credit(FMCC)")
    data = {'fordcreditapps':fordcreditapps}
    return render(request, 'fordcredit_apps.html', data)

def fordcredit_service_observations(request):
    fordcreditapps = ServiceMappingModel.objects.filter(pdo="Ford Credit(FMCC)")
    df = convert_to_dataframe(fordcreditapps)
    noauth = df[(df['adfs'].isnull()) & (df['azure_ad'].isnull())]
    html_table = noauth.to_html(index=True, border=True, classes='table')

    data = {'html':html_table}
    return render(request, 'fordcredit_service_obs.html', data)

def add_app(request):  
    if request.method == "POST":  
        form = ServiceMappingForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/gcp-service-mappings')  
            except:  
                pass
    else:  
        form = ServiceMappingForm()  
    return render(request,'index.html',{'form':form})  
 
def total_apps(request):  
    apps = ServiceMappingModel.objects.all()  
    return render(request,"show.html",{'apps':apps})  
 
def edit_app(request, id):  
    app = ServiceMappingModel.objects.get(id=id)  
    return render(request,'edit.html', {'app':app})  
 
def update_app(request, id):  
    app = ServiceMappingModel.objects.get(id=id)  
    form = ServiceMappingForm(request.POST, instance = app)  
    if form.is_valid():  
        form.save()  
        return redirect("/gcp-service-mappings")
    else:
        errors = form.errors
    data = {'app': app, 'errors':errors}      
    return render(request, 'edit.html', data )  
     
def destroy_app(request, id):  
    app = ServiceMappingModel.objects.get(id=id)  
    app.delete()  
    return redirect("/gcp-service-mappings")  