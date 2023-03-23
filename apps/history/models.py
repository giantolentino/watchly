from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    feedback = models.TextField(blank=True)
    posterpath = models.CharField(max_length=255, default="")
    rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(100)]
    )
    tmdb_id = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_watched = models.DateField()
    description = models.TextField(blank=True, null=True)
    MEDIA_TYPE_CHOICES = [
        ("tv", "Tv"),
        ("movie", "Movie"),
    ]
    media_type = models.CharField(
        max_length=5,
        choices=MEDIA_TYPE_CHOICES,
        default="tv",
    )

    def __str__(self):
        return self.title


class Tv(Entry):
    pass


class Movie(Entry):
    pass
