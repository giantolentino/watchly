from django.forms import ModelForm
from django import forms
from .models import Entry


class HistoryEntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [
            "title",
            "year",
            "posterpath",
            "rating",
            "tmdb_id",
            "media_type",
            "date_watched",
            "feedback",
        ]
        widgets = {
            "title": forms.HiddenInput(),
            "year": forms.HiddenInput(),
            "posterpath": forms.HiddenInput(),
            "tmdb_id": forms.HiddenInput(),
            "media_type": forms.HiddenInput(),
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
            "date_watched": forms.DateInput(attrs={"type": "date"}),
            "feedback": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "required": False}
            ),
        }
