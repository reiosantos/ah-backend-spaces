# Generated by Django 2.0.6 on 2018-08-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_is_account_verfied'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social_id',
            field=models.IntegerField(db_index=True, default=0, unique=True),
        ),
    ]
