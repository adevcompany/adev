# Generated by Django 3.0.5 on 2020-05-05 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200505_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='image_core',
        ),
        migrations.AddField(
            model_name='item',
            name='color_disponnible',
            field=models.CharField(choices=[('O', 'ORANGE'), ('R', 'RED'), ('G', 'GREEN'), ('B', 'BLACK'), ('W', 'WHITE')], default='O', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='previousfield',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]