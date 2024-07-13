from fastapi import  HTTPException
from sqlmodel import Session, select
from app.utils.auth import passwordIntoHash
from app.db.db_connector import  DB_SESSION
from app.models.user_model import User, UserModel, UserUpdateModel

### ============================================================================================================= ###

def get_users_from_db(session: DB_SESSION):

    users = session.exec(select(User)).all() 
    if not users:
        HTTPException(status_code=400, detail="User not found")
    #print('get user fun  ....' )    
    return users 

### ============================================================================================================= ###

# # Function to add a user to the database
# def add_user_in_db(user_base: UserModel, session: DB_SESSION):
#     print('add user fun  1 ....' )
#     # Convert UserModel to User instance
#     user = User(**user_base.model_dump())
#     user.user_password = passwordIntoHash(user_base.user_password)

#     print('add user fun  2 ....' , user)
#     if not user:
#         raise HTTPException(status_code=404, detail="User Not Found")
#     # Add the user to the session
#     session.add(user)
#     # Commit the session to save the user to the database
#     session.commit()
#     # Refresh the session to retrieve the new user data, including generated fields like user_id
#     session.refresh(user)
#     # Return the created user

#     print('add user fun end ....' , user)
#     return user

def add_user_in_db(user_base: UserModel, session: Session):
  
    # Convert UserModel to User instance
    #user = User(**user_base.dict())
    user = User(**user_base.model_dump())
    user.user_password = passwordIntoHash(user_base.user_password)

    print('add user fun 1 ....', user)

    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    # Add the user to the session
    session.add(user)
    # Commit the session to save the user to the database
    session.commit()
    # Refresh the session to retrieve the new user data, including generated fields like user_id
    session.refresh(user)
    print('add user fun 2 ....', user)
    return user


### ============================================================================================================= ###

def update_user_in_db(selected_id: int, user_base: UserUpdateModel, session: DB_SESSION):
    
    print('update user id fun  ....' )

    # Construct a query to select the user with the specified user_id
    user_query = select(User).where(User.user_id == selected_id)
    
    # Execute the query and get the first result
    user_statment = session.exec(user_query).first()
    
    # If no user is found with the given ID, raise a 404 HTTPException
    if not user_statment:
        raise HTTPException(status_code=404, detail="User is unavailable")
    
    # Update the fields of the user with the values from the user_base object
    user_statment.user_name = user_base.user_name
    user_statment.user_email = user_base.user_email
    user_statment.user_password = passwordIntoHash(user_base.user_password)
    user_statment.address = user_base.address
    user_statment.country = user_base.country
    user_statment.phone_number = user_base.phone_number
    
    # Add the updated user instance to the session
    session.add(user_statment)
    
    # Commit the transaction to save changes to the database
    session.commit()
    
    # Refresh the session to get the updated user instance
    session.refresh(user_statment)

    print('update user fun  ....' , user_statment)
    
    # Return the updated user instance
    return user_statment



