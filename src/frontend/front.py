from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates

from fastapi.responses import RedirectResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from src.frontend.dependencies import get_current_user
from src.users.models import Users
from src.tasks.service import TaskService

router = APIRouter(
    tags=["frontend service"]
)

templates = Jinja2Templates("src/frontend/public")

@router.get("/")
async def get_main(user: Users = Depends(get_current_user)):
    if user:
        return RedirectResponse("/dashboard")
    return RedirectResponse("/auth")



@router.get("/auth")
async def index(request: Request, user: Users = Depends(get_current_user)):
    if user == None:
        return templates.TemplateResponse("index.html", {"request": request})    
    return RedirectResponse("/dashboard")


@router.get("/dashboard")
async def dashboard(request: Request, user: Users = Depends(get_current_user)):
    if user == None:
        return RedirectResponse("/auth")
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": user})

@router.get("/telegram")
async def dashboard(request: Request, user: Users = Depends(get_current_user)):
    if user == None:
        return RedirectResponse("/auth")
    return templates.TemplateResponse("telegram.html", {"request": request, "data": user})


@router.get("/tasks")
async def dashboard(request: Request, user: Users = Depends(get_current_user)):
    if user == None:
        return RedirectResponse("/auth")
    return templates.TemplateResponse("tasks.html", {"request": request, "data": user})


@router.get("/tasks/{task_id}")
async def dashboard(task_id: int, request: Request, user: Users = Depends(get_current_user)):
    task = await TaskService.find_by_id(task_id)
    if user == None:
        return RedirectResponse("/auth")
    return templates.TemplateResponse("task.html", {"request": request, "data": user, "task": task})

