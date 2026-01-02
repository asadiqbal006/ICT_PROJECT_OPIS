"""
OPIS - Ocean Plant Intelligence System
A Flask-based web application that analyzes the environmental impact of sea plants
and generates detailed Ocean Health Status reports.
"""

from flask import Flask, render_template, request, redirect, url_for
from ocean_calculator import calculate_ocean_health

app = Flask(__name__)


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

