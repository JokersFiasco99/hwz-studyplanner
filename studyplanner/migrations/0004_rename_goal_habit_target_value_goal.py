# Generated by Django 5.1.4 on 2024-12-21 07:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyplanner', '0003_habit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='goal',
            new_name='target_value',
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('target_value', models.IntegerField(default=0)),
                ('current_value', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('habit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='studyplanner.habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
