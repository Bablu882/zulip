# Generated by Django 3.2.4 on 2021-06-14 12:12

from django.db import migrations, models
from django.db.backends.postgresql.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps


def make_zero_invalid_for_message_delete_limit(
    apps: StateApps, schema_editor: DatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    Realm.DEFAULT_MESSAGE_CONTENT_DELETE_LIMIT_SECONDS = 600

    Realm.objects.filter(
        allow_message_deleting=True, message_content_delete_limit_seconds=0
    ).update(message_content_delete_limit_seconds=None)

    Realm.objects.filter(
        allow_message_deleting=False, message_content_delete_limit_seconds=0
    ).update(
        message_content_delete_limit_seconds=Realm.DEFAULT_MESSAGE_CONTENT_DELETE_LIMIT_SECONDS
    )


def reverse_make_zero_invalid_for_message_delete_limit(
    apps: StateApps, schema_editor: DatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    Realm.DEFAULT_MESSAGE_CONTENT_DELETE_LIMIT_SECONDS = 600

    Realm.objects.filter(
        allow_message_deleting=True, message_content_delete_limit_seconds=None
    ).update(message_content_delete_limit_seconds=0)


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("zerver", "0353_remove_realm_default_twenty_four_hour_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="realm",
            name="message_content_delete_limit_seconds",
            field=models.IntegerField(default=600, null=True),
        ),
        migrations.RunPython(
            make_zero_invalid_for_message_delete_limit,
            reverse_code=reverse_make_zero_invalid_for_message_delete_limit,
            elidable=True,
        ),
        migrations.AlterField(
            model_name="realm",
            name="message_content_delete_limit_seconds",
            field=models.PositiveIntegerField(default=600, null=True),
        ),
    ]
