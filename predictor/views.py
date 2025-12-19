from django.shortcuts import render
from .forms import PredictionForm
from .utils import load_model, USD_TO_INR
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
            
            # Region: Map Indian regions to US regions (Model expected inputs)
            # North India -> Northwest
            # South India -> Southeast
            # West India -> Southwest
            # East India -> Northeast (Reference category: 0, 0, 0)
            
            region_northwest = 1 if region == 'north' else 0
            region_southeast = 1 if region == 'south' else 0
            region_southwest = 1 if region == 'west' else 0
            
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
            }]) 

            # Load model
            try:
                model = load_model()
                prediction_usd = model.predict(input_data)[0]
                
                # Convert to INR
                prediction_inr = prediction_usd * USD_TO_INR
                
                # Format: Round to 2 decimals
                result = f"{prediction_inr:,.2f}" 
            except Exception as e:
                result = f"Error: {str(e)}"
    else:
        form = PredictionForm()

    return render(request, 'predictor/home.html', {'form': form, 'result': result})
