# Generated by Django 3.2.9 on 2021-11-29 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='weekofhabit',
            name='friday_hours',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weekofhabit',
            name='habit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit'),
        ),
        migrations.AlterField(
            model_name='weekofhabit',
            name='monday_hours',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weekofhabit',
            name='saturday_hours',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weekofhabit',
            name='sunday_hours',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weekofhabit',
            name='thursday_hours',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weekofhabit',
            name='tuesday_hours',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weekofhabit',
            name='wednesday_hours',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
