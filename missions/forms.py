from django import forms

from .models import Misison

class MissionForm(forms.ModelForm):
    class Meta:
        model = Misison
        fields = '__all__'
        widgets = {
           'name':        forms.TextInput(attrs={'class': 'form-control space-input', 'placeholder': 'Ex: Artemis IV'}),
            'launch_date': forms.DateInput(attrs={'class': 'form-control space-input', 'type': 'date'}),
            'destination': forms.TextInput(attrs={'class': 'form-control space-input', 'placeholder': 'Ex: Marte, Lua, Órbita LEO'}),
            'state':       forms.Select(attrs={'class': 'form-select space-input'}),
            'crew':        forms.Textarea(attrs={'class': 'form-control space-input', 'rows': 4, 'placeholder': 'Um astronauta por linha'}),
            'payload':     forms.Textarea(attrs={'class': 'form-control space-input', 'rows': 3, 'placeholder': 'Descreva os equipamentos e instrumentos'}),
            'duration':    forms.TextInput(attrs={'class': 'form-control space-input', 'placeholder': 'Ex: 180 dias'}),
            'cost':        forms.NumberInput(attrs={'class': 'form-control space-input', 'placeholder': '0.00'}),
            'status_info': forms.Textarea(attrs={'class': 'form-control space-input', 'rows': 4, 'placeholder': 'Informações detalhadas sobre o status atual'}),

        }
class MissionSearchForm(forms.Form):
    date_from = forms.DateField(
        required=False,
        label="Data Inicial",
        widget=forms.DateInput(attrs={'class': 'form-control space-input', 'type': 'date'})
    )
    date_to = forms.DateField(
        required=False,
        label="Data Final",
        widget=forms.DateInput(attrs={'class': 'form-control space-input', 'type': 'date'})
    )