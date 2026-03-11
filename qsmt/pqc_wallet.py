import hashlib
import secrets

def generate_pqc_keypair():
    private_key = secrets.token_hex(32)
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    return private_key, public_key

def generate_pqc_address(public_key):
    h = hashlib.sha256(public_key.encode()).hexdigest()
    return "pqc1" + h[:40]