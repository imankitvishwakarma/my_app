# Generated by Django 4.1 on 2022-09-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("folio2", "0003_rename_project_projects"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="project_img",
            field=models.ImageField(upload_to="img"),
        ),
        migrations.AlterField(
            model_name="skills",
            name="skill_logo",
            field=models.ImageField(upload_to="img"),
        ),
    ]
