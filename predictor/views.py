from django.shortcuts import render
from .forms import PredictionForm
from .utils import load_model
import pandas as pd

def predict(request):
    result = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get data
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            bmi = form.cleaned_data['bmi']
            children = form.cleaned_data['children']
            smoker = form.cleaned_data['smoker']
            region = form.cleaned_data['region']

            # Preprocessing
            # Sex: male=0, female=1
            sex_val = 0 if sex == 'male' else 1
            
            # Smoker: yes=1, no=0
            smoker_val = 1 if smoker == 'yes' else 0
            
            # Region: One-hot encoding manual mapping
            # Columns: age, sex, bmi, children, smoker, region_northwest, region_southeast, region_southwest
            region_northwest = 1 if region == 'northwest' else 0
            region_southeast = 1 if region == 'southeast' else 0
            region_southwest = 1 if region == 'southwest' else 0
            # northeast is 0, 0, 0 (reference category)

            # Create DataFrame for prediction
            input_data = pd.DataFrame([{
                'age': age,
                'sex': sex_val,
                'bmi': bmi,
                'children': children,
                'smoker': smoker_val,
                'region_northwest': region_northwest,
                'region_southeast': region_southeast,
                'region_southwest': region_southwest
            }]) # Notes: columns must match training order. 'region_northeast' is implied by all 0s.

            # Load model
            try:
                model = load_model()
                prediction = model.predict(input_data)[0]
                result = round(prediction, 2)
            except Exception as e:
                result = f"Error: {str(e)}"
    else:
        form = PredictionForm()

    return render(request, 'predictor/home.html', {'form': form, 'result': result})
