# Generated by Django 4.2 on 2023-06-21 13:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='profiles.profile')),
            ],
        ),
    ]
