from app.core.jwt_handler import (
    create_access_tokens,
    verify_access_token
)

token = create_access_tokens(
    {
        "sub": "admin@estategpt.com"
    }
)

print("TOKEN")
print(token)

print()

payload = verify_access_token(token)


print("PAYLOAD")
print(payload)