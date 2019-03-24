# Generated by Django 2.1.7 on 2019-03-23 16:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('GN', 'GENERAL'), ('TF', 'TRUE/FALSE'), ('SA', 'SHORT ANSWER'), ('CM', 'COMMENT')], default='GN', max_length=2)),
                ('content', models.TextField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Classroom')),
            ],
        ),
    ]