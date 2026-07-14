from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.jwt_handler import verify_access_token
from app.db.database import get_db
from app.repositeries.user_repositery import get_user_by_email


security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
):
    token = credentials.credentials
    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    
    email = payload.get("sub")

    user = get_user_by_email(db, email)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return user