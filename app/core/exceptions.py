from fastapi import HTTPException

UserNotFoundException = HTTPException(status_code=404, detail='Пользователь не найден')
IncorrectPasswordException = HTTPException(status_code=401, detail='Не верный пароль')
TokenExpiredException = HTTPException(status_code=401, detail='Токен истек')
ValidateCredentialsException = HTTPException(
    status_code=403, detail='Не удалось проверить учетные данные', headers={'WWW-Authenticate': 'Bearer'}
)
NoRightsException = HTTPException(status_code=403, detail='Нет прав')