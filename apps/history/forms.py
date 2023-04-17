from django.forms import ModelForm
from django import forms
from .models import Entry
from datetime import date


class HistoryEntryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HistoryEntryForm, self).__init__(*args, **kwargs)
        today = date.today().strftime("%Y-%m-%d")
        self.fields["date_watched"].initial = today

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
            "description",
            "feedback",
        ]
        widgets = {
            "title": forms.HiddenInput(),
            "year": forms.HiddenInput(),
            "posterpath": forms.HiddenInput(),
            "tmdb_id": forms.HiddenInput(),
            "media_type": forms.HiddenInput(),
            "description": forms.HiddenInput(),
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
            "date_watched": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "feedback": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "required": False}
            ),
        }


class UpdateHistoryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["rating", "date_watched", "feedback"]
        widgets = {
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
            "date_watched": forms.DateInput(attrs={"class": "form-control"}),
            "feedback": forms.Textarea(attrs={"class": "form-control", "rows": 8}),
        }
