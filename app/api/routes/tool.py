from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/tool", tags=["tools"])


@router.get("")
def tool_check() -> dict[str, str]:
    return {"status": "ok", "service": "blogsvc"}
# check further
@router.get("/path")
def tool_check() -> dict[str, str]:
    return {"status": "ok", "service": "blogsvc", "path": "/tool/path"}
# somegi
    # running for post request
class ToolRequest(BaseModel):
    name: str
    action: str


@router.post(path="")
def tool_check(request: ToolRequest) -> dict[str, str]:
    return {
        "status": "ok",
        "service": "blogsvc",
        "name": request.name,
        "action": request.action
    }

