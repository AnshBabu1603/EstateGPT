from app.core.jwt_handler import create_access_tokens

token = create_access_tokens(
    {
        "sub": "admin@estategpt.com"
    }
)

print(token)