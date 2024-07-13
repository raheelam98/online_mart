from datetime import datetime, timedelta, timezone
from sqlmodel import select
from fastapi import HTTPException

from app.models.admin_model import AdminLoginForm, Admin, AdminCreateModel
from app.db.db_connector import DB_SESSION

from app.settings import ADMIN_EXPIRE_TIME, ADMIN_SECRET_KEY, ALGORITHM
from jose import jwt

from app.utils.auth import passwordIntoHash

### ============================================================================================================= ###

# def get_admin_from_db(session: DB_SESSION):
#     print('admin .......')
#     admin_list = session.exec(select(Admin)).all() 
#     if not admin_list:
#         HTTPException(status_code=400, detail="Admin not found")
#     print('admin list ..', admin_list)    
#     return admin_list 


# ### ============================================================================================================= ###

# # Function to add a user to the database
# def add_admin_in_db(admin_form: AdminCreateModel, session:DB_SESSION):
    
#     # Convert AdminCreateModel to admin instance
#     admin = Admin(**admin_form.model_dump())

#     if not (admin_form.admin_secret == ADMIN_SECRET_KEY):
#         raise HTTPException(status_code=404, detail="")
#     admin_exist = session.exec(select(Admin).where(
#         Admin.admin_email == admin_form.admin_email)).one_or_none()
#     if admin_exist:
#         raise HTTPException(status_code=404, detail="")

#     admin.admin_name = admin_form.admin_name
#     admin.admin_email = admin_form.admin_email
#     admin.admin_password = passwordIntoHash(admin_form.admin_password)
#     #admin.admin_password = admin_form.admin_password
    
#     print(f'Admin Detail {admin}')


#     # if not admin:
#     #     raise HTTPException(status_code=404, detail="Admin Not Found")
    
#     # Add the user to the session
#     session.add(admin)
#     # Commit the session to save the user to the database
#     session.commit()
#     # Refresh the session to retrieve the new user data, including generated fields like user_id
#     session.refresh(admin)
#     # Return the created user

#     print("admin  ", admin)

#     return admin

# ### ============================================================================================================= ###

def generateToken(admin: Admin,  expires_delta: timedelta):
    expire = datetime.now(timezone.utc) + expires_delta
    expire_delta = int(expire.timestamp())
    payload = {
        "admin_name": admin.admin_name,
        "admin_email": admin.admin_email,
        "exp": expire_delta
    }
    headers = {
        "secret": ADMIN_SECRET_KEY,
        #"kid": admin.admin_kid,
        #"iss": admin.admin_ki
    }
    token = jwt.encode(payload, ADMIN_SECRET_KEY, algorithm=ALGORITHM, headers=headers)

    print("admin token ",token)

    return token


### ============================================================================================================= ###

def admin_verify(admin_form: AdminLoginForm, session: DB_SESSION):
    admin_email = admin_form.admin_email
    admin_password = admin_form.admin_password

    if not (admin_form.admin_secret == ADMIN_SECRET_KEY):
        raise HTTPException(status_code=404, detail="Invalid admin secret")

    admin = session.exec(select(Admin).where(
        (Admin.admin_email == admin_email)
        and (Admin.admin_password == admin_password)
    )).one_or_none()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found from this details!")
    
    token = generateToken(admin, expires_delta= ADMIN_EXPIRE_TIME)

    return {
        "admin_token": token,
        "type": "bearer"
    }

### ============================================================================================================= ###


### ============================================================================================================= ###



### ============================================================================================================= ###

### ============================================================================================================= ###
# def generateToken(admin: Admin, admin_secret: str, expires_delta: timedelta) -> str:
#     expire = datetime.now(timezone.utc) + expires_delta
#     payload = {
#         "admin_name": admin.admin_name,
#         "admin_email": admin.admin_email,
#         "exp": expire
#     }
#     headers = {
#         "kid": admin.admin_kid,
#         # "secret": admin_secret,
#         "iss": admin.admin_kid
#     }
#     token = jwt.encode(payload, admin_secret, algorithm=ALGORITHM, headers=headers)
#     return token

### ============================================================================================================= ###

# def admin_verify(admin_form: AdminLoginForm, session: DB_SESSION):
#     admin_email: str = admin_form.admin_email
#     admin_password: str = admin_form.admin_password

#     if not (admin_form.admin_secret == ADMIN_SECRET_KEY):
#         raise HTTPException(status_code=404, detail="Invalid admin secret")

#     admin = session.exec(select(Admin).where(
#         (Admin.admin_email == admin_email)
#         and (Admin.admin_password == admin_password)
#     )).one_or_none()

#     if not admin:
#         raise HTTPException(status_code=404, detail="Admin not found from this details!")
#     token = generateToken(admin, admin_form.admin_secret, ADMIN_EXPIRE_TIME)

#     return {
#         "admin_token": token,
#         "type": "bearer"
#     }


### ============================================================================================================= ###

# def create_admin(admin_form: AdminCreateModel, session: DB_SESSION):
#     if not (admin_form.admin_secret == ADMIN_SECRET_KEY):
#         raise HTTPException(status_code=404, detail="Invalid admin secret")
#     admin_exist = session.exec(select(Admin).where(
#         Admin.admin_email == admin_form.admin_email)).one_or_none()
#     if admin_exist:
#         raise HTTPException(status_code=404, detail="Admin already exists with this email")
#     admin = Admin(
#         admin_name=admin_form.admin_name,
#         admin_email=admin_form.admin_email,
#         admin_password=admin_form.admin_password
#     )
#     session.add(admin)
#     session.commit()
#     session.refresh(admin)
#     # create_consumer_in_kong(admin.admin_name)
#     # create_jwt_credential_in_kong(
#     #     admin.admin_name, admin.admin_kid, admin_form.admin_secret)
#     return admin

### ============================================================================================================= ###





