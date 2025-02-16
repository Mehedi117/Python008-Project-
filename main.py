def recommend_fertilizer(crop_type, soil_quality):
    """Recommends a fertilizer based on crop type and soil quality."""
    fertilizers = {
        "wheat": {"poor": "NPK 10-26-26", "moderate": "DAP", "rich": "Urea"},
        "rice": {"poor": "Ammonium Sulfate", "moderate": "Superphosphate", "rich": "Potash"},
        "corn": {"poor": "NPK 20-20-20", "moderate": "Urea", "rich": "Compost"}
    }
    return fertilizers.get(crop_type.lower(), {}).get(soil_quality.lower(), "No suitable fertilizer found")


def recommend_pesticide(pest_symptoms):
    """Recommends a pesticide based on pest symptoms."""
    pesticides = {
        "yellow leaves": "Neem Oil Spray",
        "holes in leaves": "Bacillus Thuringiensis",
        "wilting plants": "Copper Fungicide",
        "brown spots": "Sulfur Fungicide"
    }
    return pesticides.get(pest_symptoms.lower(), "No suitable pesticide found")


# User Input
crop = input("Enter crop type (wheat/rice/corn): ").strip().lower()
soil = input("Enter soil quality (poor/moderate/rich): ").strip().lower()
pest = input("Enter pest symptom (yellow leaves/holes in leaves/wilting plants/brown spots): ").strip().lower()

fertilizer = recommend_fertilizer(crop, soil)
pesticide = recommend_pesticide(pest)

print(f"Recommended Fertilizer: {fertilizer}")
print(f"Recommended Pesticide: {pesticide}")
