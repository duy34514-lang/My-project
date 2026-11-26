from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from app.core.config import Settings


def hash_password(password: str) -> str:
    hashcode_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(hashcode_bytes, salt).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def creat_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_endcode = data.copy()
    expire = datetime.now(
        timezone.utc) + (expires_delta or timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_endcode.update({"exp": expire})

    return jwt.encode(to_endcode, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)


def decode_eccess_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY,
                             algorithms=[Settings.ALGORITHM])

        return payload
    except jwt.PyJWKError:
        return None
