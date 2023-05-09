# Generated by Django 4.1.7 on 2023-04-11 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeBe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('desc', models.TextField(max_length=255)),
                ('categories', models.CharField(choices=[('Latte', 'Latte'), ('Cappuccino', 'Cappuccino'), ('Espresso', 'Espresso')], max_length=150)),
                ('picture', models.FileField(default='defaultcoffeebe.jpg', upload_to='blog_photos')),
                ('time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoffeeBe.user')),
            ],
        ),
    ]