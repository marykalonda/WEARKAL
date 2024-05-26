# Generated by Django 5.0.6 on 2024-05-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_patron_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='couturier',
            old_name='adresseatel',
            new_name='adresse_atelier',
        ),
        migrations.RenameField(
            model_name='couturier',
            old_name='first_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='couturier',
            old_name='last_name',
            new_name='nom_atelier',
        ),
        migrations.RemoveField(
            model_name='couturier',
            name='numero',
        ),
        migrations.AddField(
            model_name='couturier',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='couturier',
            name='nom_complet',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='couturier',
            name='nom_populaire',
            field=models.CharField(default='exit', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='couturier',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
    ]