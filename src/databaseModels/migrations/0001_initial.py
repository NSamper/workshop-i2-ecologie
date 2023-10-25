# Generated by Django 4.0.4 on 2023-10-25 19:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('impact_score', models.IntegerField(blank=True, null=True)),
                ('date_in', models.DateTimeField()),
                ('date_out', models.DateTimeField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ObjectItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('material', models.CharField(choices=[('MET', 'Metal'), ('WOO', 'Wood'), ('PLA', 'Plastic'), ('CHM', 'Chemical Compound')], max_length=3)),
                ('state', models.CharField(choices=[('RAW', 'Raw material'), ('RFM', 'Refined Material'), ('IPR', 'In processing'), ('PRP', 'Processed piece'), ('FIN', 'Final State')], max_length=3)),
                ('category', models.CharField(blank=True, max_length=3, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductChain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('currStep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currStep', to='databaseModels.companymodel')),
                ('lastStep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lastStep', to='databaseModels.companymodel')),
                ('nextStep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nextStep', to='databaseModels.companymodel')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object', to='databaseModels.objectitem')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('companymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='databaseModels.companymodel')),
                ('transportType', models.CharField(choices=[('STTRU', 'Standard Truck'), ('RFTRU', 'Refrigirated Truck'), ('STTRA', 'Standard Train'), ('STBOA', 'Standard Boat'), ('STPLA', 'Standard Plane')], max_length=5)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('objectItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='databaseModels.objectitem')),
            ],
            options={
                'abstract': False,
            },
            bases=('databaseModels.companymodel',),
        ),
        migrations.CreateModel(
            name='Transform',
            fields=[
                ('companymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='databaseModels.companymodel')),
                ('process', models.CharField(choices=[('CUT', 'Cut'), ('SME', 'Smelt'), ('TRE', 'Chemical Treatment'), ('SHP', 'Reshape'), ('ASB', 'Assemble')], max_length=3)),
                ('objectItem_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input', to='databaseModels.objectitem')),
                ('objectItem_output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output', to='databaseModels.objectitem')),
            ],
            options={
                'abstract': False,
            },
            bases=('databaseModels.companymodel',),
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('companymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='databaseModels.companymodel')),
                ('storageType', models.CharField(blank=True, choices=[('WRH', 'Warehouse'), ('RWH', 'Refrigerated Warehouse'), ('HWH', 'Heated Warehouse')], max_length=3, null=True)),
                ('objectItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectItem', to='databaseModels.objectitem')),
            ],
            options={
                'abstract': False,
            },
            bases=('databaseModels.companymodel',),
        ),
        migrations.CreateModel(
            name='Extracts',
            fields=[
                ('companymodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='databaseModels.companymodel')),
                ('extract_type', models.CharField(choices=[('MIN', 'Mining'), ('CHO', 'Chopping'), ('CHE', 'Chemical Creation')], max_length=3)),
                ('objectItem_output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extr_output', to='databaseModels.objectitem')),
            ],
            options={
                'abstract': False,
            },
            bases=('databaseModels.companymodel',),
        ),
    ]
