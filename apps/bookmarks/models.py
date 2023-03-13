from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    posterpath = models.CharField(max_length=255, default="")
    tmdb_id = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    priority = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    MEDIA_TYPE_CHOICES = [
        ("tv", "Tv"),
        ("movie", "Movie"),
    ]
    media_type = models.CharField(
        max_length=5,
        choices=MEDIA_TYPE_CHOICES,
        default="tv",
    )

    # Each record must have unique combo of following fields.
    class Meta:
        unique_together = (("user", "tmdb_id", "media_type"),)

    def __str__(self):
        return self.title


class Tv(Bookmark):
    pass


class Movie(Bookmark):
    pass
