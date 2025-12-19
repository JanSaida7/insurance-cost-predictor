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
    age = forms.IntegerField(label='Age', min_value=0, max_value=120, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    sex = forms.ChoiceField(label='Sex', choices=SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}))
    bmi = forms.FloatField(label='BMI', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'BMI'}))
    children = forms.IntegerField(label='Children', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}))
    smoker = forms.ChoiceField(label='Smoker', choices=SMOKER_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Smoker Status'}))
    region = forms.ChoiceField(label='Region', choices=REGION_CHOICES, widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Region'}))
