# Generated by Django 3.1.3 on 2020-11-12 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0004_auto_20201112_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='toy.element'),
        ),
    ]
