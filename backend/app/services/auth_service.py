from app.core.security import verify_password
from app.core.jwt_handler import create_access_tokens
from app.repositeries.user_repositery import get_user_by_email

def login_user(db, email, password):

    user = get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None
    
    token = create_access_tokens(
        {
            "sub": user.email
        }
    )

    return token