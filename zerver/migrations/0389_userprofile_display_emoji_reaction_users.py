# Generated by Django 3.2.12 on 2022-04-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0388_preregistrationuser_created_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="realmuserdefault",
            name="display_emoji_reaction_users",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="display_emoji_reaction_users",
            field=models.BooleanField(default=True),
        ),
    ]
