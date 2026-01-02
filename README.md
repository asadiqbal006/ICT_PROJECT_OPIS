# ICT_PROJECT_OPIS

**OPIS - Ocean Plant Intelligence System**

A comprehensive system for analyzing the environmental impact of sea plants and generating detailed Ocean Health Status reports. The project includes both a Flask web application and a FastAPI REST API.

## Features

- 🌊 Analyze ocean health based on sea plant characteristics
- 📊 Calculate oxygen production, carbon absorption, and marine life support metrics
- ⚠️ Generate warnings for critical environmental conditions
- 🌐 Web interface (Flask) for interactive analysis
- 🔌 REST API (FastAPI) for programmatic access

## Project Structure

```
.
├── app.py                 # Flask web application
├── api.py                 # FastAPI REST API
├── ocean_calculator.py    # Shared calculation logic
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates for Flask
│   ├── index.html
│   └── result.html
└── static/               # Static files (CSS, etc.)
    └── css/
        └── style.css
```

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Flask Web Application

Run the Flask web application:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### FastAPI REST API

Run the FastAPI REST API:

```bash
python api.py
```

Or using uvicorn directly:

```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

#### API Documentation

FastAPI provides automatic interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

#### API Endpoints

- `GET /` - API information
- `GET /health` - Health check endpoint
- `POST /api/analyze` - Analyze ocean health
- `GET /api/plant-types` - Get available plant types

#### Example API Request

```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "plant_type": "Kelp",
    "density": "High",
    "pollution": "Low",
    "temperature": "Normal"
  }'
```

#### Example API Response

```json
{
  "oxygen_production": 85.0,
  "carbon_absorption": 95.0,
  "marine_life_support": 90.0,
  "status_message": "🌊 Healthy Ocean",
  "status_color": "success",
  "status_description": "Ocean ecosystem is functioning well with optimal plant density and minimal environmental stressors.",
  "warnings": [],
  "plant_type": "Kelp",
  "density": "High",
  "pollution": "Low",
  "temperature": "Normal"
}
```

## Plant Types

- **Seagrass**: Excellent carbon absorption, good oxygen production
- **Kelp**: High efficiency in all metrics
- **Algae**: Moderate efficiency, watch for algal blooms at high density
- **Phytoplankton**: Excellent oxygen production

## Technologies

- **Flask**: Web framework for the user interface
- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for FastAPI
- **Bootstrap 5**: Frontend framework for responsive design

## Running Both Services

You can run both Flask and FastAPI simultaneously on different ports:

- Flask: `http://localhost:5000` (web interface)
- FastAPI: `http://localhost:8000` (REST API)
