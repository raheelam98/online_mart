from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from sqlmodel import select

from app.settings import SECRET_KEY, ADMIN_SECRET_KEY, ALGORITHM
from app.db.db_connector import DB_SESSION
from app.models.auth_admin_model import Admin


### ============================================================================================================= ###

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def decode_jwt(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded
    except JWTError:
        raise HTTPException(
            status_code=401, detail="Could not validate credentials")

### ============================================================================================================= ###
#
    
def admin_required(token: Annotated[str, Depends(oauth2_scheme)], session: DB_SESSION):
    headers = jwt.get_unverified_headers(token)
    admin_secret = headers.get("secret")
    #admin_name = headers.get("name")
    admin_kid = headers.get("kid")
    payload = decode_jwt(token)
    admin = session.exec(select(Admin).where(Admin.admin_name == payload.get(
        "admin_name")).where(Admin.admin_email == payload.get("admin_email")).where(Admin.admin_kid == admin_kid)).one_or_none()
    print(admin)
    #print(admin_name)
    print(f"Admin Secret : {admin_secret}")

    if not admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    

    if not (str(admin_secret) == str(ADMIN_SECRET_KEY)):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return payload


### ============================================================================================================= ###






### ============================================================================================================= ###

### ============================================================================================================= ###



# from datetime import datetime, timedelta, timezone

# def generateToken(admin: Admin,  expires_delta: timedelta) -> str:
#     expire = datetime.now(timezone.utc) + expires_delta
#     payload = {
#         "admin_name": admin.admin_name,
#         "admin_email": admin.admin_email,
#         "exp": expire
#     }
#     headers = {
#         "kid": admin.admin_kid,
#         "iss": admin.admin_kid
#     }
#     token = jwt.encode(payload, ADMIN_SECRET_KEY, algorithm=ALGORITHM, headers=headers)

#     print("admin token ",token)

#     return token


### ============================================================================================================= ###



# def decode_jwt11(token: str):
#     try:
#         decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         return decoded
#     except JWTError:
#         raise HTTPException(
#             status_code=401, detail="Could not validate credentials")


# def admin_required11(token: Annotated[str, Depends(oauth2_scheme)], session: DB_SESSION):
#     headers = jwt.get_unverified_headers(token)
#     admin_secret = headers.get("secret")
#     admin_kid = headers.get("kid")
#     payload = decode_jwt(token)
#     admin = session.exec(select(Admin).where(Admin.admin_name == payload.get(
#         "admin_name")).where(Admin.admin_email == payload.get("admin_email")).where(Admin.admin_kid == admin_kid)).one_or_none()
#     print(admin)
#     print(admin_secret)

#     if not admin:
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     if not (str(admin_secret) == str(ADMIN_SECRET_KEY)):
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     return payload
