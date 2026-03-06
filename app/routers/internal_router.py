"""Internal API endpoints for health checks and other internal operations."""

from fastapi import APIRouter

router = APIRouter(prefix="/internal", tags=["Internal"])


@router.get("/health", response_model=None)
async def root() -> dict[str, str]:
    """Root endpoint that returns a simple message."""
    return {
        "status": "Healthy",
        "message": "App is running!",
        # 'api': settings.PROJECT_NAME,
        # 'version': settings.PROJECT_VERSION,
        # # 'environment': settings.ENV,
    }
