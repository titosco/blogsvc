from fastapi import FastAPI

from app.api.routes import health, tool
# for testing tools

from app.api.routes import tool

app = FastAPI(
    title="blogsvc",
    version="0.1.0",
    description="Simple blog CMS backend",
)

app.include_router(health.router)
# testing for tools routes
app.include_router(tool.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to titosco"}
