# Generated by Django 3.2.4 on 2024-08-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10)),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
