# Generated by Django 4.2.6 on 2023-10-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowboards', '0008_snowboard_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snowboard',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate-Advanced', 'Intermediate Advanced')], default='Intermediate-Advanced', max_length=30),
        ),
        migrations.AlterField(
            model_name='snowboard',
            name='style',
            field=models.CharField(choices=[('Park', 'Park'), ('Freeride', 'Free Ride'), ('All mountain', 'All Mountain')], default='All mountain', max_length=15),
        ),
    ]
