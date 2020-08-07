from django import forms
from .models import Orang


class OrangForm(forms.ModelForm):
    class Meta:
        model = Orang
        fields = "__all__"
