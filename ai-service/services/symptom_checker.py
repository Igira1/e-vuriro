def check_symptoms(symptoms_text):
    # Simple keyword-based analysis
    symptoms = symptoms_text.lower()
    conditions = []
    if "fever" in symptoms and "cough" in symptoms:
        conditions.append({"condition": "Common Cold", "risk": "Low"})
    if "chest pain" in symptoms:
        conditions.append({"condition": "Heart Issue", "risk": "High"})
    # Add more logic
    return {"possible_conditions": conditions, "recommendation": "Consult a doctor"}