# Generated by Django 3.1.7 on 2021-02-27 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='bird',
            old_name='species',
            new_name='breed',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bird')),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='feeding date')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bird')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='bird',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]
