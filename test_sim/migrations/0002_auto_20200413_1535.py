# Generated by Django 3.0.3 on 2020-04-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_sim', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsim',
            name='inputs',
        ),
        migrations.AddField(
            model_name='testsim',
            name='b_zero',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testsim',
            name='f',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testsim',
            name='loop_radius',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testsim',
            name='r',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testsim',
            name='seconds',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testsim',
            name='csv',
            field=models.FileField(upload_to='csv'),
        ),
    ]