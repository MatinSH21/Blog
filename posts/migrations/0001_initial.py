# Generated by Django 3.2 on 2023-05-19 12:56

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('image', models.ImageField(default='default.jpg', upload_to='post_pics/%Y/%m/%d/', verbose_name='image')),
                ('content', models.TextField(verbose_name='content')),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('is_edited', models.BooleanField(default=False, verbose_name='edited')),
                ('like', models.IntegerField(default=0, verbose_name='like')),
                ('dislike', models.IntegerField(default=0, verbose_name='dislike')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='posts.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'Comments',
                'ordering': ['-date_created'],
            },
        ),
    ]
