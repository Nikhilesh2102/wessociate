# Generated by Django 4.2.2 on 2023-09-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_idea_idea_posted_by_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='idea_posted_by_mail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]