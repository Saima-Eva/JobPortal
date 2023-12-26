# Generated by Django 5.0 on 2023-12-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_remove_jobseekerprofile_profile_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_model',
            name='description',
        ),
        migrations.AddField(
            model_name='job_model',
            name='company_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job_model',
            name='deadline',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job_model',
            name='job_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job_model',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='media/profile_pic'),
        ),
        migrations.AddField(
            model_name='job_model',
            name='qualifications',
            field=models.TextField(null=True),
        ),
    ]