# Generated by Django 2.2 on 2019-04-16 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('book_pulish_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Roles_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=30)),
                ('Roles_gerden', models.BooleanField()),
                ('Roles_Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP1_demo1.Book_list')),
            ],
        ),
    ]
