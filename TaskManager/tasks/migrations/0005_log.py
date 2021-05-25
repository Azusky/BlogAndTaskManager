# Generated by Django 3.1.8 on 2021-05-24 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_assign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_data', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='tasks.task')),
            ],
            options={
                'ordering': ['start_data'],
            },
        ),
    ]
