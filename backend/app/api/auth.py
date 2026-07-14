from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.db.database import get_db
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.services.auth_service import login_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    token = login_user(
        db,
        request.email,
        request.password
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }

from app.core.dependencies import get_current_user
from app.models.user import User

@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return {
        "user_id": current_user.user_id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role_id": current_user.role_id
    }