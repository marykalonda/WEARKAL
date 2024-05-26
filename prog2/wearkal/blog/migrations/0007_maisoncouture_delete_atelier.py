# Generated by Django 5.0.6 on 2024-05-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_couturier_topic_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaisonCouture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('photo_atel', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('telephone', models.CharField(max_length=15)),
                ('specialisation', models.CharField(choices=[('CoutureHomme', 'Couturehomme'), ('CoutureFemme', 'Couturefemme'), ('CoutureMixte', 'Couturemixte')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('site_web', models.URLField()),
                ('description', models.TextField()),
                ('date_creation', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='atelier',
        ),
    ]
