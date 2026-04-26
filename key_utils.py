import hashlib

def generate_key(password: str):
    # Convert password → SHA-256 → bytes
    key = hashlib.sha256(password.encode()).digest()
    return key