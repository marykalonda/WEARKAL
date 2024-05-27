# Generated by Django 5.0.6 on 2024-05-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_visite', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='Ajouter_commentaire',
        ),
    ]