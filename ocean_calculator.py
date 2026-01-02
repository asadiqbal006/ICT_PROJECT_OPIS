"""
Shared calculation module for OPIS - Ocean Plant Intelligence System
Contains the core logic for calculating ocean health metrics.
Used by both Flask web app and FastAPI REST API.
"""


def calculate_ocean_health(plant_type, density, pollution, temperature):
    """
    Calculate three key ocean health metrics based on user inputs.
    
    Args:
        plant_type (str): Type of sea plant (Seagrass, Kelp, Algae, Phytoplankton)
        density (str): Plant density level (Low, Medium, High)
        pollution (str): Water pollution level (Low, Medium, High)
        temperature (str): Water temperature (Normal, High)
    
    Returns:
        dict: Contains oxygen_production, carbon_absorption, marine_life_support,
              status_message, status_color, and warnings
    """
    
    # Base efficiency scores for different plant types (0-100 scale)
    # Phytoplankton and Kelp have higher oxygen production
    # Seagrass and Kelp excel at carbon absorption
    plant_efficiency = {
        'Seagrass': {'oxygen': 70, 'carbon': 90, 'support': 85},
        'Kelp': {'oxygen': 85, 'carbon': 95, 'support': 90},
        'Algae': {'oxygen': 60, 'carbon': 50, 'support': 40},
        'Phytoplankton': {'oxygen': 90, 'carbon': 70, 'support': 75}
    }
    
    # Density multipliers
    density_multipliers = {
        'Low': 0.6,
        'Medium': 0.8,
        'High': 1.0
    }
    
    # Get base values for the selected plant type
    base_oxygen = plant_efficiency[plant_type]['oxygen']
    base_carbon = plant_efficiency[plant_type]['carbon']
    base_support = plant_efficiency[plant_type]['support']
    
    # Apply density multiplier
    density_mult = density_multipliers[density]
    
    # Calculate initial metrics
    oxygen_production = base_oxygen * density_mult
    carbon_absorption = base_carbon * density_mult
    marine_life_support = base_support * density_mult
    
    # Special rule: Algal Bloom effect
    # High density Algae reduces Marine Life Support (simulates harmful algal bloom)
    if plant_type == 'Algae' and density == 'High':
        marine_life_support *= 0.5  # Reduce by 50% due to algal bloom
    
    # Pollution penalty: High pollution reduces all metrics by 40%
    if pollution == 'High':
        oxygen_production *= 0.6  # 40% reduction
        carbon_absorption *= 0.6
        marine_life_support *= 0.6
    elif pollution == 'Medium':
        oxygen_production *= 0.8  # 20% reduction
        carbon_absorption *= 0.8
        marine_life_support *= 0.8
    
    # Temperature penalty: High temperature affects all metrics
    if temperature == 'High':
        oxygen_production *= 0.85  # 15% reduction
        carbon_absorption *= 0.85
        marine_life_support *= 0.85
    
    # Ensure values are within 0-100 range
    oxygen_production = min(100, max(0, round(oxygen_production, 1)))
    carbon_absorption = min(100, max(0, round(carbon_absorption, 1)))
    marine_life_support = min(100, max(0, round(marine_life_support, 1)))
    
    # Generate warnings
    warnings = []
    if plant_type == 'Seagrass' and temperature == 'High':
        warnings.append("⚠️ Warning: Seagrass is highly sensitive to elevated temperatures. Consider monitoring closely.")
    
    if plant_type == 'Algae' and density == 'High':
        warnings.append("⚠️ Algal Bloom Alert: High density Algae can lead to harmful algal blooms, reducing marine life support.")
    
    # Determine overall ocean health status
    avg_score = (oxygen_production + carbon_absorption + marine_life_support) / 3
    
    if pollution == 'High' and temperature == 'High':
        status_message = "🌊 Ocean Collapse Warning"
        status_color = "danger"
        status_description = "Critical conditions detected: High pollution combined with elevated temperatures pose severe risks to ocean ecosystems."
    elif pollution == 'High' or temperature == 'High' or avg_score < 60:
        status_message = "🌊 Unstable Ocean"
        status_color = "warning"
        status_description = "Ocean conditions are unstable. Environmental stressors are impacting ecosystem health."
    else:
        status_message = "🌊 Healthy Ocean"
        status_color = "success"
        status_description = "Ocean ecosystem is functioning well with optimal plant density and minimal environmental stressors."
    
    return {
        'oxygen_production': oxygen_production,
        'carbon_absorption': carbon_absorption,
        'marine_life_support': marine_life_support,
        'status_message': status_message,
        'status_color': status_color,
        'status_description': status_description,
        'warnings': warnings,
        'plant_type': plant_type,
        'density': density,
        'pollution': pollution,
        'temperature': temperature
    }

