# Generated by Django 2.2.5 on 2022-12-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221210_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Farsi', 'Farsi')], default='Farsi', max_length=10),
        ),
    ]