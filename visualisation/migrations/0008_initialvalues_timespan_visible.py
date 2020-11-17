# Generated by Django 3.1.3 on 2020-11-17 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0007_auto_20201024_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x0', models.BooleanField(default=True)),
                ('x1', models.BooleanField(default=True)),
                ('x2', models.BooleanField(default=False)),
                ('x3', models.BooleanField(default=False)),
                ('x4', models.BooleanField(default=False)),
                ('system', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visualisation.system')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSpan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.FloatField(default=0)),
                ('end', models.FloatField(default=0)),
                ('system', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visualisation.system')),
            ],
        ),
        migrations.CreateModel(
            name='InitialValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x0', models.FloatField(default=0)),
                ('x1', models.FloatField(default=0)),
                ('x2', models.FloatField(default=0)),
                ('x3', models.FloatField(default=0)),
                ('x4', models.FloatField(default=0)),
                ('system', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visualisation.system')),
            ],
        ),
    ]
