# Generated by Django 3.0.5 on 2020-05-06 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab_repo', '0002_auto_20200506_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='next_element',
            field=models.OneToOneField(null='True', on_delete=django.db.models.deletion.SET_NULL, to='lab_repo.Element'),
        ),
    ]