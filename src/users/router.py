from fastapi import APIRouter, Response, Depends

from src.users.service import UserService
from src.users.models import Users
from src.users.schemas import SUserAuth, SUserReg
from src.users.exceptions import UserAlredyExistsException, IncorrectUserOrPassException

from src.users.auth import * 
from src.users.dependencies import * 

router = APIRouter(
    prefix="/users",
    tags=["users api service"]
)

@router.post("/register")
async def register_user(user_data: SUserReg):
    existing_user = await UserService.find_one_or_none(login=user_data.login)
    if existing_user:
        raise UserAlredyExistsException
    if user_data.status in ["admin", "employe"]:
        hashed_password = get_password_hash(user_data.password)
        await UserService.add(
            login=user_data.login, 
            hashed_password=hashed_password, 
            status=user_data.status, 
            aspro_id=user_data.aspro_id,
            fullname=user_data.fullname
        )
        return {"status": 200, "detail": f"{user_data.status} was created"}
    return {"status": 409}
 

@router.post("/login")
async def register_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.login, user_data.password)
    if not user:
        raise IncorrectUserOrPassException
    
    access_token = create_access_token({"sub": str(user.id)})
    
    response.set_cookie("booking_access_token", access_token, httponly=True)

    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return {"status": "logout"}


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user


@router.get("/employes")
async def get_all_users():
    return await UserService.find_all(status="employe")