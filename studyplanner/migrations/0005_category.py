# Generated by Django 5.1.4 on 2024-12-21 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyplanner', '0004_rename_goal_habit_target_value_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyplanner.goal')),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyplanner.habit')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyplanner.task')),
            ],
        ),
    ]
