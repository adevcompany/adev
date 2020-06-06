# Generated by Django 3.0.5 on 2020-05-05 21:50

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200505_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetail',
            name='color',
            field=models.CharField(choices=[('P', 'PURPLE'), ('R', 'RED'), ('G', 'GREEN'), ('B', 'BLACK'), ('W', 'WHITE')], max_length=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='color_disponnible',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('P', 'PURPLE'), ('R', 'RED'), ('G', 'GREEN'), ('B', 'BLACK'), ('W', 'WHITE')], max_length=10),
        ),
    ]