# Generated by Django 3.2.4 on 2021-06-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210604_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_grade',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
