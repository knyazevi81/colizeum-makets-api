from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from src.frontend.front import router as front_router
from src.users.router import router as users_router
from src.tg.router import router as tg_router
from src.tasks.router import router as task_router

from src.frontend.dependencies import *

app = FastAPI(
    title="Colizeum makets"
)


app.mount("/static", StaticFiles(directory="src/frontend/public/static"), "static")


app.include_router(front_router)
app.include_router(users_router)
app.include_router(tg_router)
app.include_router(task_router)

#https://stackoverflow.com/questions/63511413/fastapi-redirection-for-trailing-slash-returns-non-ssl-link 
