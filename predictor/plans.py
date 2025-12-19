import random

def get_recommended_plans(predicted_cost_inr):
    """
    Generates 3 simulated insurance plans based on the predicted medical cost.
    
    Args:
        predicted_cost_inr (float): The predicted medical cost in INR.
        
    Returns:
        list: A list of 3 dictionary objects representing Silver, Gold, and Platinum plans.
    """
    
    # Base Premium Calculation (Simulated)
    # Insurance premium is roughly 1-2% of the cover amount + risk factors
    # Here we assume the 'predicted_cost' is the *Expected Application Medical Cost*, 
    # so we structure the Cover Amount to be sufficient for that.
    
    recommended_cover = max(500000, predicted_cost_inr * 1.5) # Minimum 5 Lakhs or 1.5x predicted
    
    # Round to nearest Lakh
    recommended_cover = round(recommended_cover / 100000) * 100000
    
    base_premium = recommended_cover * 0.02 # 2% of cover as base annual premium

    plans = [
        {
            'name': 'Silver Health Saver',
            'provider': 'SecureWell India',
            'tier': 'silver',
            'cover_amount': f"₹ {int(recommended_cover*0.8):,}",
            'premium': f"₹ {int(base_premium * 0.8):,}",
            'features': ['Basic Hospitalization', 'No Room Rent Capping', 'COVID-19 Cover'],
            'color': 'secondary',
            'badge': 'Economy'
        },
        {
            'name': 'Gold Shield Plus',
            'provider': 'LifeGuard Assure',
            'tier': 'gold',
            'cover_amount': f"₹ {int(recommended_cover):,}",
            'premium': f"₹ {int(base_premium):,}",
            'features': ['Comprehensive Cover', 'Free Health Checkup', 'Pre & Post Hospitalization', 'Ayush Treatment'],
            'color': 'warning',
            'badge': 'Most Popular'
        },
        {
            'name': 'Platinum Elite Global',
            'provider': 'Royal Care Insurance',
            'tier': 'platinum',
            'cover_amount': f"₹ {int(recommended_cover * 1.5):,}",
            'premium': f"₹ {int(base_premium * 1.4):,}",
            'features': ['Global Coverage', 'Zero Depreciation', 'Maternity Cover', 'OPD Expenses', 'Priority Claims'],
            'color': 'info',
            'badge': 'Premium'
        }
    ]
    
    return plans
