"""Internal API endpoints for health checks and other internal operations."""

from typing import Any

from fastapi import APIRouter, status

router = APIRouter(tags=["Internal"])


@router.get("/health", response_model=None)
async def root() -> dict[str, str]:
    """Root endpoint that returns a simple message."""
    return {
        "status": "Healthy",
        "message": "App is running!",
    }


@router.get("/saldo/membresia", response_model=Any, status_code=status.HTTP_200_OK)
async def consult_membership() -> dict[str, Any]:
    """Consult membership endpoint."""
    return {
        "estado_membresia": 200,
        "estado_app_renta": 300,
        "estado_proyexus": 600,
        "estado_hosting ": 500,
    }
