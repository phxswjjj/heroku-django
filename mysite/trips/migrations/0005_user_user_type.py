# Generated by Django 3.0.2 on 2020-01-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20200127_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('CB', '社團'), ('GUEST', '球友')], default='CB', max_length=5),
        ),
    ]