from datetime import datetime, timedelta
import jwt
from settings.config import settings  # Assuming the settings are here

# Corrected function: No need for `.upper()` on Enum values
def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    
    # Ensure role is passed as string from Enum directly (no .upper())
    if 'role' in to_encode:
        to_encode['role'] = to_encode['role']  # already a string, no need for .upper()
        
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({"exp": expire})
    
    # Encoding the JWT
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

def decode_token(token: str):
    try:
        decoded = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        return decoded
    except jwt.PyJWTError:
        return None
