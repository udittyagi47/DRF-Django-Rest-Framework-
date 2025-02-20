# Generated by Django 4.2.16 on 2025-02-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('mail_id', models.EmailField(max_length=254, unique=True)),
                ('student_photo', models.ImageField(blank=True, null=True, upload_to='student_photos/')),
            ],
        ),
    ]
