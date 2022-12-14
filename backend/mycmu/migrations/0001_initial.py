# Generated by Django 4.0.3 on 2022-04-16 19:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_post_title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('career_post_text', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200, null=True)),
                ('visa_sponsor', models.BooleanField(null=True)),
                ('creation_time', models.DateTimeField()),
                ('career_post_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='career_post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_year', models.IntegerField()),
                ('course_semester', models.CharField(max_length=200)),
                ('course_college', models.CharField(max_length=200)),
                ('course_department', models.CharField(max_length=200)),
                ('course_number', models.IntegerField()),
                ('course_section', models.CharField(max_length=200)),
                ('course_instructor_firstname', models.CharField(max_length=200)),
                ('course_instructor_lastname', models.CharField(max_length=200)),
                ('course_name', models.CharField(max_length=200)),
                ('course_level', models.CharField(max_length=200)),
                ('course_response_num', models.IntegerField()),
                ('course_hour', models.FloatField(default=1.7514)),
                ('course_teaching_rate', models.FloatField(default=1.7514)),
                ('course_overall_rate', models.FloatField(default=1.7514)),
            ],
        ),
        migrations.CreateModel(
            name='CoursePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_post_title', models.CharField(max_length=200)),
                ('course_post_text', models.CharField(max_length=200)),
                ('creation_time', models.DateTimeField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_id', to='mycmu.course')),
                ('course_post_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=200)),
                ('profile_picture', models.FileField(blank=True, upload_to='')),
                ('user_point', models.IntegerField(default=0)),
                ('followers', models.ManyToManyField(blank=True, default=None, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following_career_post', models.ManyToManyField(blank=True, default=None, related_name='career_post', to='mycmu.careerpost')),
                ('following_course_post', models.ManyToManyField(blank=True, default=None, related_name='course_post', to='mycmu.coursepost')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_creators', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('creation_time', models.DateTimeField(default=datetime.datetime(2022, 4, 16, 19, 54, 47, 445525))),
                ('from_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_user_id', to=settings.AUTH_USER_MODEL)),
                ('to_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_comment_text', models.CharField(max_length=200)),
                ('creation_time', models.DateTimeField()),
                ('course_comment_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_comment_user', to=settings.AUTH_USER_MODEL)),
                ('course_post_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_post_id', to='mycmu.coursepost')),
            ],
        ),
        migrations.CreateModel(
            name='CareerComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_comment_text', models.CharField(max_length=200)),
                ('creation_time', models.DateTimeField()),
                ('career_comment_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='career_comment_user', to=settings.AUTH_USER_MODEL)),
                ('career_post_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_id', to='mycmu.careerpost')),
            ],
        ),
    ]
