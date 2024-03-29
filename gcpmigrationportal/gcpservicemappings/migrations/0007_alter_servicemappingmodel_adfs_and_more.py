# Generated by Django 5.0.3 on 2024-03-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcpservicemappings', '0006_alter_servicemappingmodel_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='adfs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='apigee',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='app_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='app_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='app_pipeline',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='architecture_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='automated_testing_after_deploy',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='automated_testing_before_deploy',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='availability',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='azure_ad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='big_query',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='business_remarks',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='business_value',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='checkmarx',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_armor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_build',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_dns',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_function',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_logging',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_monitoring',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_run',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_scheduler',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloud_storage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloudsql_mssql_ee',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloudsql_mssql_se',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cloudsql_pg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='comparision_notes',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='compute_engine',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='crunch_42',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='current_state_db',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='current_state_tech_stack',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='cycode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='data_flow',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='deployment_topology',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='deployment_topology_tobedeleted',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='deviation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='devsecops_pipeline',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='downtime',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='external_load_balancer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='fire_store',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='fossa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='future_state_tech_stack',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='gcp_caas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='iac_pipeline',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='in_scope',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='internal_load_balancer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='memory_store',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='migration_category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='migration_roadmap',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='migration_scope',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='mongo_db_atlas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='monitoring',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='no_of_cloud_run_ms',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='onprem_caas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='onprem_db',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='pdo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='planned_launch_date',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='pub_sub',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='remarks',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='secret_manager',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='sla',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='sonarqube',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='sre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='target_db',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicemappingmodel',
            name='verification',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
