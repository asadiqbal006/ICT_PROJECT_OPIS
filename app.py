"""
OPIS - Ocean Plant Intelligence System
A Flask-based web application that analyzes the environmental impact of sea plants
and generates detailed Ocean Health Status reports.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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


@app.route('/')
def index():
    """Render the main input form."""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Process form data and calculate ocean health metrics."""
    plant_type = request.form.get('plant_type')
    density = request.form.get('density')
    pollution = request.form.get('pollution')
    temperature = request.form.get('temperature')
    
    # Validate inputs
    if not all([plant_type, density, pollution, temperature]):
        return redirect(url_for('index'))
    
    # Calculate ocean health metrics
    results = calculate_ocean_health(plant_type, density, pollution, temperature)
    
    return render_template('result.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)

