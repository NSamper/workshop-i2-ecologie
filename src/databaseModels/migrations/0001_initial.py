# Generated by Django 4.0.4 on 2023-10-23 18:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectItem',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('dedd0d32-cc7d-48fd-987f-2eaf74d08121'), primary_key=True, serialize=False, unique=True)),
                ('material', models.CharField(choices=[('MET', 'Metal'), ('WOO', 'Wood'), ('PLA', 'Plastic'), ('CHM', 'Chemical Compound')], max_length=3)),
                ('state', models.CharField(choices=[('RAW', 'Raw material'), ('RFM', 'Refined Material'), ('IPR', 'In processing'), ('PRP', 'Processed piece'), ('FIN', 'Final State')], max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('dedd0d32-cc7d-48fd-987f-2eaf74d08121'), primary_key=True, serialize=False, unique=True)),
                ('impact_score', models.IntegerField(blank=True, null=True)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('transportType', models.CharField(choices=[('STTRU', 'Standard Truck'), ('RFTRU', 'Refrigirated Truck'), ('STTRA', 'Standard Train'), ('STBOA', 'Standard Boat'), ('STPLA', 'Standard Plane')], max_length=5)),
                ('objectItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='databaseModels.objectitem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transform',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('dedd0d32-cc7d-48fd-987f-2eaf74d08121'), primary_key=True, serialize=False, unique=True)),
                ('impact_score', models.IntegerField(blank=True, null=True)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('process', models.CharField(choices=[('CUT', 'Cut'), ('SME', 'Smelt'), ('TRE', 'Chemical Treatment'), ('SHP', 'Reshape'), ('ASB', 'Assemble')], max_length=3)),
                ('objectItem_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input', to='databaseModels.objectitem')),
                ('objectItem_output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output', to='databaseModels.objectitem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('dedd0d32-cc7d-48fd-987f-2eaf74d08121'), primary_key=True, serialize=False, unique=True)),
                ('impact_score', models.IntegerField(blank=True, null=True)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('objectItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectItem', to='databaseModels.objectitem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductChain',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('dedd0d32-cc7d-48fd-987f-2eaf74d08121'), primary_key=True, serialize=False, unique=True)),
                ('lastStep', models.UUIDField()),
                ('currStep', models.UUIDField()),
                ('nextStep', models.UUIDField()),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object', to='databaseModels.objectitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
