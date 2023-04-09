# Generated by Django 4.2 on 2023-04-09 17:18

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, validators=[core.validators.correct_email_validator], verbose_name='эл.почта'),
        ),
    ]
