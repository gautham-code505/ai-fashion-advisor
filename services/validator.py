# services/validator.py

def validate_preferences(form_data):
    errors = []
    
    required_fields = ["gender", "skin_tone", "body_shape", "occasion", "budget"]
    for field in required_fields:
        if not form_data.get(field):
            errors.append(f"{field.replace('_', ' ').title()} is required.")
            
    try:
        if form_data.get("budget"):
            int(form_data.get("budget"))
    except ValueError:
        errors.append("Budget must be a valid number.")
        
    return errors
