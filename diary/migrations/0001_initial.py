# Generated by Django 4.2.19 on 2025-03-07 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_movie_movie_year'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='FirstName', max_length=200)),
                ('last_name', models.CharField(default='LastName', max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('this_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_day', models.CharField(default='1st Jan 2025', max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('which_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='home.movie')),
                ('which_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
