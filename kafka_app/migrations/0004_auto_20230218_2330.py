# Generated by Django 3.2.18 on 2023-02-18 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kafka_app', '0003_auto_20230218_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signalmodel',
            name='machine_id',
        ),
        migrations.RemoveField(
            model_name='signalmodel',
            name='sensor_id',
        ),
        migrations.AddField(
            model_name='signalmodel',
            name='exhauster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='machine', to='kafka_app.machinemodel'),
        ),
        migrations.AddField(
            model_name='signalmodel',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='kafka_app.sensormodel'),
        ),
        migrations.AlterField(
            model_name='signalmodel',
            name='type',
            field=models.CharField(choices=[('ANALOG', 0), ('DIGITAL', 1)], max_length=255),
        ),
    ]