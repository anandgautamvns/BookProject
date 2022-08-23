# Generated by Django 4.1 on 2022-08-20 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('image_title', models.CharField(blank=True, max_length=120)),
                ('uploded_at', models.DateTimeField(auto_now_add=True)),
                ('pizzeria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizzeria_images', to='stores.pizzeria')),
            ],
            options={
                'ordering': ['-uploded_at'],
            },
        ),
    ]
