from sqlalchemy.orm import Session
from src.models.user import UserModel
from src.schemas.user import UserRegister
from src.utils.hashing import hash_password , verify_password

def create_user(db : Session , user : UserRegister):

    existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if existing_user:
        return None
    
    new_user = UserModel(
        username = user.username,
        email = user.email,
        password = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def authenticate_user(db : Session , email : str , password : str):

    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user:
        return None
    
    if not verify_password(password , user.password):
        return None
    
    return user