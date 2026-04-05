from fastapi import FastAPI

from app.api.routes.health import router as health_router

app = FastAPI(
    title="blogsvc",
    version="0.1.0",
    description="Simple blog CMS backend",
)

app.include_router(health_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to titosco"}
