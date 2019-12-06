# Generated by Django 2.2.6 on 2019-12-06 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0006_auto_20191201_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Create at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('beers', models.ManyToManyField(blank=True, related_name='special_ingredients', to='beers.Beer')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_specialingredient_createdby', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_specialingredient_modifiedby', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Special Ingredient',
                'verbose_name_plural': 'Special Ingredients',
                'ordering': ['-name'],
            },
        ),
        migrations.DeleteModel(
            name='SpecialIngredients',
        ),
    ]
