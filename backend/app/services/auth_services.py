from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repostories import user_repo
from app.schemas.user import UserCreat
from app.core.security import hash_password, verify_password, creat_access_token


def register_user(db: Session, user_in: UserCreat):
    existing_user = user_repo.get_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="tên đăng nhập đã tồn tại"
        )

    hash_pwd = hash_password(user_in.password)
    return user_repo.create_user(db, user_in.username, user_in.email, hash_pwd)


def authenticate_user(db: Session, email: str, password: str) -> str:
    user = user_repo.get_by_email(db, email)
    if not user or not verify_password(password=password, hashed_password=user.hash_passwork):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="sai tên đăng nhập hoặc mật khẩu"
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="tài khoản đã bị khóa"
        )

    return creat_access_token(data={"sub": user.username, "role": user.role})
