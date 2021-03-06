# Generated by Django 2.1 on 2018-08-25 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminOtziv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='GuestOtziv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=20000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='adminotziv',
            name='guestOtziv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guest_otziv.GuestOtziv'),
        ),
    ]
