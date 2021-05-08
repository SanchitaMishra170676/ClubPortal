# Generated by Django 3.1.4 on 2021-05-08 08:02

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
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('announcement', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic_name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/Dashboard/SubTopic/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='upcomingHackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('mode', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], default='offline', max_length=10)),
                ('description', models.TextField(max_length=150)),
                ('deadline', models.DateTimeField()),
                ('image', models.ImageField(blank=True, upload_to='media/dashboard/upcomingHackathon/')),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=255, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.subtopic')),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updateName', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=255, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.course')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('resources', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.topic'),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('email', models.EmailField(max_length=255)),
                ('otherInfo1', models.CharField(blank=True, max_length=300)),
                ('otherInfo2', models.CharField(blank=True, max_length=300)),
                ('facebookURL', models.CharField(blank=True, max_length=150)),
                ('twitterURL', models.CharField(blank=True, max_length=150)),
                ('instagramURL', models.CharField(blank=True, max_length=150)),
                ('linkedinURL', models.CharField(blank=True, max_length=150)),
                ('skypeURL', models.CharField(blank=True, max_length=150)),
                ('githubURL', models.CharField(blank=True, max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('techUsed', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('teamMembers', models.CharField(max_length=100)),
                ('videoURL', models.CharField(blank=True, max_length=100)),
                ('githubURL', models.CharField(max_length=100)),
                ('yourRole', models.CharField(blank=True, max_length=100)),
                ('time', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/Dashboard/project/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf', models.FileField(upload_to='media/Dashboard/PDF/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.subtopic')),
            ],
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hackathonName', models.CharField(max_length=150)),
                ('achievement', models.CharField(choices=[('first', 'first'), ('second', 'second'), ('top 5 ', 'top 5'), ('participation', 'participation'), ('others', 'others')], max_length=150)),
                ('prize', models.CharField(blank=True, max_length=250)),
                ('certificate', models.CharField(blank=True, max_length=200)),
                ('teamMembers', models.CharField(blank=True, max_length=300)),
                ('teamName', models.CharField(blank=True, max_length=200)),
                ('techStack', models.CharField(blank=True, max_length=100)),
                ('yourRole', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default='', upload_to='media/Dashboard/hackathon/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('paragraph1', models.TextField()),
                ('paragraph2', models.TextField()),
                ('image', models.ImageField(upload_to='media/Dashboard/ContentImages/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.subtopic')),
            ],
        ),
        migrations.CreateModel(
            name='ClubProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('rather not say', 'rather not say')], default='male', max_length=50)),
                ('branch', models.CharField(blank=True, choices=[('CO', 'CO'), ('IT', 'IT'), ('CSIT', 'CSIT'), ('CSE', 'CSE'), ('EC', 'EC'), ('ME', 'ME'), ('CE', 'CE'), ('EN', 'EN'), ('other', 'other')], default='CO', max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('college_email', models.EmailField(max_length=200, unique=True)),
                ('personal_email', models.EmailField(blank=True, max_length=200)),
                ('domain', models.CharField(max_length=200)),
                ('batch', models.CharField(default='2020-2024', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='media/dashboard/clubprofile/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hostel_status', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_mentor', models.BooleanField(default=False)),
                ('courses', models.ManyToManyField(blank=True, to='dashboard.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('domain', models.CharField(max_length=100)),
                ('highlights', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('code', models.TextField(blank=True)),
                ('subHeading', models.CharField(blank=True, max_length=200)),
                ('quote', models.CharField(blank=True, max_length=150)),
                ('quoteBy', models.CharField(blank=True, max_length=150)),
                ('tag1', models.CharField(blank=True, max_length=100)),
                ('tag2', models.CharField(blank=True, max_length=100)),
                ('tag3', models.CharField(blank=True, max_length=100)),
                ('Thumbimage1', models.ImageField(blank=True, default='', upload_to='media/Dashboard/article/')),
                ('Thumbimage2', models.ImageField(blank=True, default='', null=True, upload_to='media/Dashboard/article/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_approved', models.BooleanField(default=False)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievementName', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Technical', 'Technical'), ('Non-Technical', 'Non-Technical'), ('Others', 'Others'), ('Academics', 'Academics')], max_length=100)),
                ('role', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('certiURL', models.CharField(blank=True, max_length=150)),
                ('image', models.ImageField(blank=True, default='', upload_to='media/Dashboard/achievement/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
