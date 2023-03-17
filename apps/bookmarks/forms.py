from django import forms
from .models import Bookmark


class BookmarkForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, initial=1)

    class Meta:
        model = Bookmark
        fields = [
            "user",
            "title",
            "year",
            "posterpath",
            "tmdb_id",
            "description",
            "media_type",
            "priority",
        ]
        widgets = {
            "user": forms.HiddenInput(),
            "title": forms.HiddenInput(),
            "year": forms.HiddenInput(),
            "posterpath": forms.HiddenInput(),
            "tmdb_id": forms.HiddenInput(),
            "description": forms.HiddenInput(),
            "media_type": forms.HiddenInput(),
        }


class UpdateBookmarkForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)

    class Meta:
        model = Bookmark
        fields = ["priority"]
