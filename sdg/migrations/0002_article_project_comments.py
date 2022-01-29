# Generated by Django 4.0 on 2022-01-23 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sdg.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('Incompletegoals', models.TextField(blank=True)),
                ('Completegoals', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sdg.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sdg.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sdg.user')),
            ],
        ),
    ]