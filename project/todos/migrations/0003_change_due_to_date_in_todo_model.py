# Generated by Django 4.2.4 on 2023-09-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0002_remove_description_and_add_state_field_to_todo_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="due",
            field=models.DateField(blank=True, null=True, verbose_name="Due"),
        ),
    ]
