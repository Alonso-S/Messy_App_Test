# messy_app/security/insecure_ops.py
import hashlib

def insecure_hash_password(pwd: str):
    # Security violation B303: MD5 is insecure
    return hashlib.md5(pwd.encode()).hexdigest()

def insecure_eval(data):
    # B307: eval is dangerous
    return eval(data)

def insecure_random():
    # B311: random is not for security
    import random
    return random.random()
