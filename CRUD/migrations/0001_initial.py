# Generated by Django 4.0 on 2021-12-23 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettlementLogic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_item', models.TextField()),
                ('second_item', models.TextField()),
                ('result_item', models.TextField()),
            ],
            options={
                'db_table': 'SettlementLogic',
            },
        ),
    ]
