# Generated by Django 3.1.8 on 2021-05-24 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210518_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blogId',
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
            preserve_default=False,
        ),
    ]
