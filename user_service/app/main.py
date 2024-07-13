from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated

from app.models.user_model import User, UserModel, UserUpdateModel , Token
from app.controllers.crud_user import get_users_from_db, add_user_in_db, update_user_in_db
from app.controllers.auth_user import user_login

from app.db.db_connector import  create_db_and_tables ,DB_SESSION

from app.models.admin_model import Admin, AdminCreateModel, AdminLoginForm
from app.controllers.crud_admin import add_admin_in_db, get_admin_from_db

from app.controllers.auth_admin import admin_verify



### ============================================================================================================= ###

app = FastAPI(lifespan = create_db_and_tables)


@app.get('/')
def get_route():
    return "user service"

@app.get('/api/get_users', response_model=list[User])
def get_user(session:DB_SESSION):
      user_list = get_users_from_db(session)
      if not user_list:
        raise HTTPException(status_code=404, detail="User Not Found in DB")
      else:
        return user_list    
      
### ============================================================================================================= ###


@app.post("/api/add_user", response_model=User)
def add_user(new_user: UserModel, session: DB_SESSION):
    # Call the function to add the user to the database
    created_user = add_user_in_db(new_user, session)
    if not created_user:
        raise HTTPException(status_code=404, detail="Can't Add User")
    return created_user



### ============================================================================================================= ###


@app.put('/api/update_user', response_model=User)
def update_user(id:int, user_detail: UserUpdateModel, session: DB_SESSION):
    # Call the function to update the user to the database
    updated_user = update_user_in_db(id,user_detail, session )
    if not updated_user:
        raise HTTPException(status_code=404, detail="Can't Find User")
    return updated_user

### ============================================================================================================= ###

@app.post('/api/login_user', response_model= Token)
async def authenicate_user(token: Annotated[dict, Depends(user_login) ] ):
     if not token:
          HTTPException(status_code=400, detail="Try agin")
     return token   
     
### ============================================================================================================= ###

@app.get('/api/get_admins', response_model=list[Admin])
def get_admin(session:DB_SESSION):
      admin_list = get_admin_from_db(session)
      if not admin_list:
        raise HTTPException(status_code=404, detail="Not Found in DB")
      else:
        return admin_list  
      
### ============================================================================================================= ###

@app.post("/api/login_admin", response_model=dict)
def verify_admin(admin_form: AdminLoginForm, session: DB_SESSION):
    admin_token = admin_verify(admin_form, session)
    if not admin_token:
        raise HTTPException(status_code=404, detail="Admin has not verified!")
    return admin_token

### ============================================================================================================= ###

@app.post('/api/add_admin', response_model=Admin)
async def add_admin(new_admin: AdminCreateModel, session: DB_SESSION):
    # Call the function to add the admin to the database
    created_admin = add_admin_in_db(new_admin, session)
    if not created_admin:
        raise HTTPException(status_code=404, detail="Can't Add Admin")
    return created_admin

# ### ============================================================================================================= ###

# @app.get("/api/admin-verify", response_model=dict)
# def verify_admin(admin_token: Annotated[dict, Depends(admin_verify)]):
#     if not admin_token:
#         raise HTTPException(status_code=404, detail="Admin has not verified!")
#     return admin_token

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

## NOT WORKING
# @app.get('/api/get_admin', response_model=list[User])
# def get_admin(session:DB_SESSION):
#       admin_list = get_admin_from_db(session)
#       print('admin list route ..')
#       if not admin_list:
#         raise HTTPException(status_code=404, detail="admin Not Found in DB")
#       else:
#         return admin_list 



