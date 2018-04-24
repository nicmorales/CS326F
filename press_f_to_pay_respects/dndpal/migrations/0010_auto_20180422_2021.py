# Generated by Django 2.0.4 on 2018-04-23 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dndpal', '0009_auto_20180419_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterclass',
            name='hitpoints',
            field=models.PositiveIntegerField(default=10, help_text='Enter the hit die for this class'),
        ),
        migrations.AlterField(
            model_name='characterclassspelllist',
            name='spell_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dndpal.Spell'),
        ),
    ]