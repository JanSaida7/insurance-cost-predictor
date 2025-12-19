from django import forms

SEX_CHOICES = [('male', 'Male'), ('female', 'Female')]
SMOKER_CHOICES = [('yes', 'Yes'), ('no', 'No')]
REGION_CHOICES = [
    ('north', 'North India'),
    ('south', 'South India'),
    ('east', 'East India'),
    ('west', 'West India'),
]

class PredictionForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=0, max_value=120, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Sex', choices=SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    bmi = forms.FloatField(label='BMI', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    children = forms.IntegerField(label='Children', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    smoker = forms.ChoiceField(label='Smoker', choices=SMOKER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    region = forms.ChoiceField(label='Region', choices=REGION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
