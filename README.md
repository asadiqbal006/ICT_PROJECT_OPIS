# ICT_PROJECT_OPIS

**OPIS - Ocean Plant Intelligence System**

A comprehensive system for analyzing the environmental impact of sea plants and generating detailed Ocean Health Status reports. The project includes both a Flask web application with interactive animations and a FastAPI REST API.

## 🌟 Features

- 🌊 **Ocean Health Analysis** - Analyze ocean health based on sea plant characteristics
- 📊 **Detailed Metrics** - Calculate oxygen production, carbon absorption, and marine life support metrics
- ⚠️ **Smart Warnings** - Generate warnings for critical environmental conditions
- 🌐 **Interactive Web Interface** - Beautiful Flask web app with smooth animations
- 🔌 **REST API** - FastAPI REST API for programmatic access
- ✨ **Modern UI** - Responsive design with Bootstrap 5 and custom animations
- 📱 **Mobile Friendly** - Fully responsive design that works on all devices

## 📁 Project Structure

```
.
├── app.py                 # Flask web application
├── api.py                 # FastAPI REST API
├── ocean_calculator.py    # Shared calculation logic
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates for Flask
│   ├── index.html        # Main input form
│   └── result.html       # Results display page
└── static/               # Static files
    ├── css/
    │   └── style.css      # Custom styling with ocean theme
    └── js/
        └── animations.js  # JavaScript animations
```

## 🚀 Installation

1. **Clone or download the project**

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python --version  # Python 3.7+ required
   ```

## 💻 Usage

### Flask Web Application

Run the Flask web application:

```bash
python app.py
```

The application will be available at **`http://localhost:5000`**

**Features:**

- Interactive form with real-time validation
- Beautiful ocean-themed UI
- Smooth animations and transitions
- Responsive design for all screen sizes

### FastAPI REST API

Run the FastAPI REST API:

```bash
python api.py
```

Or using uvicorn directly:

```bash
uvicorn api:app --reload
```

The API will be available at **`http://localhost:8000`**

#### 📚 API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs` (Interactive testing)
- **ReDoc**: `http://localhost:8000/redoc` (Alternative documentation)

#### 🔗 API Endpoints

| Method | Endpoint           | Description                                |
| ------ | ------------------ | ------------------------------------------ |
| `GET`  | `/`                | API information and available endpoints    |
| `GET`  | `/health`          | Health check endpoint                      |
| `POST` | `/api/analyze`     | Analyze ocean health with parameters       |
| `GET`  | `/api/plant-types` | Get available plant types and descriptions |

#### 📝 Example API Request

**Using curl:**

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

**Using Python:**

```python
import requests

response = requests.post(
    "http://localhost:8000/api/analyze",
    json={
        "plant_type": "Kelp",
        "density": "High",
        "pollution": "Low",
        "temperature": "Normal"
    }
)
print(response.json())
```

#### 📤 Example API Response

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

## 🧪 Testing the API

### Method 1: Swagger UI (Recommended)

1. Start the API: `python api.py`
2. Open browser: `http://localhost:8000/docs`
3. Click "Try it out" on any endpoint
4. Fill parameters and click "Execute"

### Method 2: Command Line (curl)

```bash
# Health check
curl http://localhost:8000/health

# Analyze ocean health
curl -X POST "http://localhost:8000/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"plant_type": "Kelp", "density": "High", "pollution": "Low", "temperature": "Normal"}'
```

### Method 3: Python Script

```python
import requests

# Test health endpoint
response = requests.get("http://localhost:8000/health")
print(response.json())

# Test analyze endpoint
response = requests.post(
    "http://localhost:8000/api/analyze",
    json={
        "plant_type": "Seagrass",
        "density": "Medium",
        "pollution": "High",
        "temperature": "High"
    }
)
print(response.json())
```

## 🌿 Plant Types

| Plant Type        | Characteristics                                             |
| ----------------- | ----------------------------------------------------------- |
| **Seagrass**      | Excellent carbon absorption, good oxygen production         |
| **Kelp**          | High efficiency in all metrics                              |
| **Algae**         | Moderate efficiency, watch for algal blooms at high density |
| **Phytoplankton** | Excellent oxygen production                                 |

## 🎨 UI Features

### Animations

- **Fade-in effects** for cards and elements
- **Smooth progress bars** with animated fill
- **Interactive buttons** with hover effects
- **Form field animations** on focus
- **Badge pulse effects** for visual feedback
- **Number counting animation** for percentages

### Design

- Ocean-themed color scheme
- Responsive Bootstrap 5 layout
- Smooth transitions and hover effects
- Mobile-friendly interface

## 🛠️ Technologies

### Backend

- **Flask** (3.0.0) - Web framework for the user interface
- **FastAPI** (0.109.0) - Modern, fast web framework for building APIs
- **Pydantic** (2.5.3) - Data validation using Python type annotations
- **Uvicorn** (0.27.0) - ASGI server for FastAPI

### Frontend

- **Bootstrap 5** - Frontend framework for responsive design
- **Bootstrap Icons** - Icon library
- **Custom CSS** - Ocean-themed styling
- **JavaScript** - Smooth animations and interactions

## 🔄 Running Both Services

You can run both Flask and FastAPI simultaneously on different ports:

**Terminal 1:**

```bash
python app.py
# Flask running on http://localhost:5000
```

**Terminal 2:**

```bash
python api.py
# FastAPI running on http://localhost:8000
```

## 📊 How It Works

1. **User Input**: Select plant type, density, pollution level, and temperature
2. **Calculation**: System calculates three key metrics:
   - Oxygen Production (0-100%)
   - Carbon Absorption (0-100%)
   - Marine Life Support (0-100%)
3. **Analysis**: System applies environmental factors and generates warnings
4. **Results**: Display comprehensive ocean health status with visual indicators

## ⚙️ Configuration

### API Parameters

**Plant Types:**

- `Seagrass`
- `Kelp`
- `Algae`
- `Phytoplankton`

**Density Levels:**

- `Low`
- `Medium`
- `High`

**Pollution Levels:**

- `Low`
- `Medium`
- `High`

**Temperature:**

- `Normal`
- `High`

## 🐛 Troubleshooting

### API not responding?

- Check if server is running: `python api.py`
- Verify port 8000 is available
- Check terminal for error messages

### Flask app not loading?

- Ensure port 5000 is available
- Check if templates folder exists
- Verify static files are in correct location

### Import errors?

- Install all dependencies: `pip install -r requirements.txt`
- Check Python version (3.7+ required)

## 📝 License

This project is part of ICT coursework.

## 👥 Contributing

This is an academic project. For improvements or suggestions, please contact the project maintainer.

---

**Made with 🌊 for Ocean Health Analysis**
