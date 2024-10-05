from fastapi import status, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from config import settings

security = HTTPBasic()


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    password = get_password()
    if password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return True


def get_password():
    return settings.password.get_secret_value()
