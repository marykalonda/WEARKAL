# Generated by Django 5.0.2 on 2024-03-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='atelier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adresse', models.CharField(max_length=30)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='couturier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('numero', models.IntegerField(default=0)),
                ('adresseatel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='patron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomode', models.CharField(max_length=30)),
                ('explain', models.TextField(blank=True)),
                ('pub_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]