"""
OPIS - Ocean Plant Intelligence System
A Flask-based web application that analyzes the environmental impact of sea plants
and generates detailed Ocean Health Status reports.
"""

from flask import Flask, render_template, request, redirect, url_for
from ocean_calculator import calculate_ocean_health

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    """Render the main input form or process form data."""
    if request.method == 'POST':
        # Process form data and calculate ocean health metrics
        plant_type = request.form.get('plant_type')
        density = request.form.get('density')
        pollution = request.form.get('pollution')
        temperature = request.form.get('temperature')
        
        # Validate inputs
        if not all([plant_type, density, pollution, temperature]):
            return redirect(url_for('analyze'))
        
        # Calculate ocean health metrics
        results = calculate_ocean_health(plant_type, density, pollution, temperature)
        
        return render_template('result.html', results=results)
    else:
        # Render the main input form
        return render_template('index.html')


@app.route('/about')
def about():
    """Render the about us page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact us page."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

