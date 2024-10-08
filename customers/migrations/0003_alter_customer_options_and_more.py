# Generated by Django 5.1 on 2024-08-14 12:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_delete_customers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='customer_image'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
