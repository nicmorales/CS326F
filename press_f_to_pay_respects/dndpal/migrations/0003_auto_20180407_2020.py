# Generated by Django 2.0.2 on 2018-04-08 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndpal', '0002_auto_20180407_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subracefeatures',
            name='name',
            field=models.CharField(default='', help_text='Enter the name of the subrace', max_length=100, primary_key=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='damage',
            field=models.CharField(default='', help_text='Enter the damage die of this weapon', max_length=10000),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='range',
            field=models.CharField(default='', help_text='Enter the range of the weapon.', max_length=10000),
        ),
    ]