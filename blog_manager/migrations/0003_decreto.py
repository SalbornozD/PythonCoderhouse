# Generated by Django 5.1.4 on 2025-01-08 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_manager', '0002_categoria_remove_blogimage_blog_noticia_noticiaimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decreto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
