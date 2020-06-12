# Generated by Django 3.0.5 on 2020-06-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='document',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='documents',
            name='soft',
            field=models.ManyToManyField(related_name='documents', to='api.Soft'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='employee',
            field=models.ManyToManyField(related_name='employee_resource', to='api.Employee'),
        ),
        migrations.AlterField(
            model_name='soft',
            name='employee',
            field=models.ManyToManyField(related_name='employee_soft', to='api.Employee'),
        ),
    ]