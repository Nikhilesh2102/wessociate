# Generated by Django 4.2.2 on 2023-09-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_idea_idea_posted_by_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='deal_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_id', models.IntegerField(blank=True, null=True)),
                ('investor_username', models.CharField(blank=True, max_length=255, null=True)),
                ('idea_provider_username', models.CharField(blank=True, max_length=255, null=True)),
                ('investor_deal_status', models.CharField(choices=[('NONE', 'NONE'), ('ON', 'ON'), ('OFF', 'OFF')], default='NONE', max_length=4)),
                ('idea_provider_deal_status', models.CharField(choices=[('NONE', 'NONE'), ('ON', 'ON'), ('OFF', 'OFF')], default='NONE', max_length=4)),
            ],
        ),
    ]