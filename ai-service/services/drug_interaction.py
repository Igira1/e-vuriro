def check_interaction(drugs):
    # Mock interaction check
    interactions = []
    if "aspirin" in drugs and "warfarin" in drugs:
        interactions.append("Increased bleeding risk")
    return {"interactions": interactions}