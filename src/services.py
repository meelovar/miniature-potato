import hashlib


def hash_sha256_string(input_str: str) -> str:
    return hashlib.sha256(input_str.encode()).hexdigest()
