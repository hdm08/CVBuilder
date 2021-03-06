# Generated by Django 3.0.7 on 2020-11-20 12:36

import CVApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='no-img.jpg', upload_to=CVApp.models.get_upload_path)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('middle_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('birth_date', models.CharField(default='1999-12-31', max_length=20)),
                ('email', models.EmailField(default='none@email.com', max_length=254)),
                ('Address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=255)),
                ('state', models.CharField(default='', max_length=255)),
                ('Postal_Zip_Code', models.IntegerField(default='123')),
                ('Phone_Number', models.IntegerField(default='123')),
                ('ssc_school', models.CharField(default='', max_length=100)),
                ('ssc_year_of_passing', models.IntegerField(default='0')),
                ('ssc_percentage', models.FloatField(default='100')),
                ('hsc_school', models.CharField(default='', max_length=100)),
                ('hsc_year_of_passing', models.IntegerField(default='0')),
                ('hsc_percentage', models.FloatField(default='100')),
                ('ug_college', models.CharField(default='', max_length=100)),
                ('ug_collage_cgpa', models.FloatField(default='100')),
                ('ug_degree', models.CharField(default='', max_length=100)),
                ('pg_college', models.CharField(default='', max_length=100)),
                ('pg_collage_cgpa', models.FloatField(default='100')),
                ('pg_degree', models.CharField(default='', max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('any_other_qualification', models.CharField(default='', max_length=200)),
                ('internship_experience', models.CharField(default='', max_length=200)),
                ('certificates', models.FileField(blank=True, default='no-img.jpg', upload_to=CVApp.models.get_upload_path)),
                ('about_you', models.FileField(blank=True, default='no-img.jpg', upload_to=CVApp.models.get_upload_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
