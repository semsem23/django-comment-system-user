# Generated by Django 2.2.5 on 2021-06-26 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('content', models.TextField(null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, upload_to='media')),
                ('slug', models.SlugField(unique=True)),
                ('topic', models.CharField(choices=[('politique', 'Politique'), ('finance', 'Finance'), ('economique', 'Economique'), ('monde', 'Monde'), ('sport', 'Sport'), ('people', 'People'), ('santé', 'Sante'), ('actualité', 'Actualite'), ('international', 'International')], default='Politique', max_length=40)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
