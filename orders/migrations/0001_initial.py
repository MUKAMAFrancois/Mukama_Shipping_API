# Generated by Django 4.1.3 on 2023-06-03 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Electronic_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('electronic', models.CharField(choices=[('phones', 'SmartPhones'), ('laptops', 'Laptops'), ('desktops', 'Desktops'), ('appliances', 'Home appliances')], max_length=40)),
                ('description', models.CharField(default='', max_length=500)),
                ('price', models.FloatField()),
                ('weight', models.FloatField()),
                ('warranty', models.FloatField()),
                ('electronic_picture', models.ImageField(upload_to='electronics/')),
                ('district_name', models.CharField(choices=[('Kicukiro', 'Kicukiro'), ('Gasabo', 'Gasabo'), ('Nyarugenge', 'Nyarugenge')], max_length=20)),
                ('sector_name', models.CharField(choices=[('kimisagara', 'Kimisagara'), ('Nyamirambo', 'Nyamirambo'), ('Gitega', 'Gitega'), ('Kacyiru', 'Kacyiru'), ('Kanombe', 'Kanombe'), ('Masaka', 'Masaka'), ('Gikondo', 'Gikondo'), ('Muhima', 'Muhima'), ('Rwezamenyo', 'Rwezamenyo'), ('Niboye', 'Niboye'), ('Gatsata', 'Gatsata'), ('Jali', 'Jali'), ('Gisozi', 'Gisozi'), ('Kimihurura', 'Kimihurura'), ('Jabana', 'Jabana'), ('Remera', 'Remera')], max_length=30)),
                ('be_shipped', models.BooleanField(default=False, help_text='can we deliver it?, free service')),
                ('phone_number', models.PositiveBigIntegerField(null=True, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ship_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
