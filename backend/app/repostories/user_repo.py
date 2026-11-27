from sqlalchemy.orm import Session
from app.models.user import User


def get_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, username: str, email: str, hashed_password: str, role: str = "user") -> User:
    db_user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        role=role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    print(db_user)
    return db_user
