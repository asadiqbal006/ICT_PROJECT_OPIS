"""
FastAPI REST API for OPIS - Ocean Plant Intelligence System
Provides REST API endpoints for ocean health analysis.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
from ocean_calculator import calculate_ocean_health

app = FastAPI(
    title="OPIS API",
    description="Ocean Plant Intelligence System - REST API for analyzing ocean health",
    version="1.0.0"
)

# Enable CORS for all origins (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for request/response validation
class OceanHealthRequest(BaseModel):
    plant_type: Literal["Seagrass", "Kelp", "Algae", "Phytoplankton"] = Field(
        ..., description="Type of sea plant"
    )
    density: Literal["Low", "Medium", "High"] = Field(
        ..., description="Plant density level"
    )
    pollution: Literal["Low", "Medium", "High"] = Field(
        ..., description="Water pollution level"
    )
    temperature: Literal["Normal", "High"] = Field(
        ..., description="Water temperature"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "plant_type": "Kelp",
                "density": "High",
                "pollution": "Low",
                "temperature": "Normal"
            }
        }


class OceanHealthResponse(BaseModel):
    oxygen_production: float = Field(..., description="Oxygen production percentage (0-100)")
    carbon_absorption: float = Field(..., description="Carbon absorption percentage (0-100)")
    marine_life_support: float = Field(..., description="Marine life support percentage (0-100)")
    status_message: str = Field(..., description="Overall ocean health status message")
    status_color: str = Field(..., description="Status color indicator (success/warning/danger)")
    status_description: str = Field(..., description="Detailed status description")
    warnings: list[str] = Field(..., description="List of warnings if any")
    plant_type: str = Field(..., description="Input plant type")
    density: str = Field(..., description="Input density level")
    pollution: str = Field(..., description="Input pollution level")
    temperature: str = Field(..., description="Input temperature")


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Welcome to OPIS API - Ocean Plant Intelligence System",
        "version": "1.0.0",
        "endpoints": {
            "analyze": "/api/analyze",
            "docs": "/docs",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "OPIS API"}


@app.post("/api/analyze", response_model=OceanHealthResponse)
async def analyze_ocean_health(request: OceanHealthRequest):
    """
    Analyze ocean health based on plant type, density, pollution, and temperature.
    
    - **plant_type**: Type of sea plant (Seagrass, Kelp, Algae, Phytoplankton)
    - **density**: Plant density level (Low, Medium, High)
    - **pollution**: Water pollution level (Low, Medium, High)
    - **temperature**: Water temperature (Normal, High)
    
    Returns detailed ocean health metrics including:
    - Oxygen production percentage
    - Carbon absorption percentage
    - Marine life support percentage
    - Overall status and warnings
    """
    try:
        results = calculate_ocean_health(
            plant_type=request.plant_type,
            density=request.density,
            pollution=request.pollution,
            temperature=request.temperature
        )
        return OceanHealthResponse(**results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating ocean health: {str(e)}")


@app.get("/api/plant-types")
async def get_plant_types():
    """Get available plant types."""
    return {
        "plant_types": ["Seagrass", "Kelp", "Algae", "Phytoplankton"],
        "descriptions": {
            "Seagrass": "Excellent carbon absorption, good oxygen production",
            "Kelp": "High efficiency in all metrics",
            "Algae": "Moderate efficiency, watch for algal blooms at high density",
            "Phytoplankton": "Excellent oxygen production"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

