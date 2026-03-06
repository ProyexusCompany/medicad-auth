from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers import internal_router

app = FastAPI()

app.include_router(internal_router.router)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Auth App is running!"}


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def docs() -> RedirectResponse:
    """Redirect to docs."""
    return RedirectResponse(url="/docs")
