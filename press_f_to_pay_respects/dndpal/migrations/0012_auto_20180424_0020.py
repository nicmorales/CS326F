# Generated by Django 2.0.4 on 2018-04-24 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndpal', '0011_spell_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterclass',
            name='hitpoints',
            field=models.PositiveIntegerField(default=10, help_text='Enter the hit points for this class'),
        ),
    ]