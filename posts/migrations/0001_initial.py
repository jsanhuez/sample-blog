# Generated by Django 2.2.12 on 2020-05-18 02:41

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_header', models.ImageField(upload_to='posts/photos')),
                ('post', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('categories', models.ManyToManyField(to='categories.Category')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]