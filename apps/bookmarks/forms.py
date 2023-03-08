from django import forms
from .models import Bookmark


class BookmarkForm(forms.ModelForm):
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
            "priority": forms.TextInput(
                attrs={
                    "type": "text",
                    "inputmode": "numeric",
                    "pattern": "[0-9]+",
                }
            ),
        }


class UpdateBookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = [
            "priority",
        ]
        widgets = {
            "priority": forms.TextInput(
                attrs={
                    "type": "text",
                    "inputmode": "numeric",
                    "pattern": "[0-9]+",
                }
            ),
        }
