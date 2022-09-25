# Generated by Django 4.1 on 2022-09-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("folio2", "0006_alter_projects_project_img_alter_skills_skill_logo"),
    ]

    operations = [
        migrations.CreateModel(
            name="aboutme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("about_img", models.ImageField(blank=True, upload_to="img/")),
                ("about_resume", models.FileField(upload_to="resume/")),
            ],
        ),
    ]
