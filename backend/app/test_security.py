from app.core.security import (
    hash_password,
    verify_password
)

password = "EstateGPT123"

hashed = hash_password(password)
print(password)

print()

print("Hashed Password: ")
print(hashed)

print()

print("Password Match: ")
print(
    verify_password(
        password,
        hashed
    )
)