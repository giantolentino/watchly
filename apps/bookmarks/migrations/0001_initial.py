# Generated by Django 4.1.6 on 2023-03-06 19:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bookmark",
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
                ("title", models.CharField(max_length=100)),
                ("year", models.IntegerField(default=0)),
                ("posterpath", models.CharField(default="", max_length=255)),
                ("tmdb_id", models.IntegerField(default=0, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "priority",
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                (
                    "media_type",
                    models.CharField(
                        choices=[("tv", "Tv"), ("movie", "Movie")],
                        default="tv",
                        max_length=5,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "tmdb_id", "media_type")},
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "bookmark_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="bookmarks.bookmark",
                    ),
                ),
            ],
            bases=("bookmarks.bookmark",),
        ),
        migrations.CreateModel(
            name="Tv",
            fields=[
                (
                    "bookmark_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="bookmarks.bookmark",
                    ),
                ),
            ],
            bases=("bookmarks.bookmark",),
        ),
    ]