from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.user import UserCreat, UserLogin, UserResponse, Token
from app.services import auth_services
from app.core.deps import get_current_user, require_role
from app.models.user import User

router = APIRouter(prefix="/api/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse)
def register(user_in: UserCreat, db: Session = Depends(get_db)):
    return auth_services.register_user(db, user_in)


@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    token = auth_services.authenticate_user(
        db, credentials.email, credentials.password)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/employer-only")
def employer_area(user: User = Depends(require_role(["employer", "admin"]))):
    return {"messagee" f'khu vực dành cho người thuê việc: {user.email}'}
