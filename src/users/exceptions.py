from fastapi import HTTPException, status


UserAlredyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует"
)

IncorrectUserOrPassException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверное введен пароль или логин"
)
 
   