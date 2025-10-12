import pathlib

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_env_path():
    path = pathlib.Path(__file__)
    return path.parent.absolute() / ".env"


def get_env():
    path = get_env_path()
    env_dict = {}

    with open(path, "rt+") as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            item = line.split("=")
            if len(item) <= 1:
                continue
            env_dict[item[0]] = item[1]
    return env_dict


def get_secret_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return kdf.derive(password.encode())


def encrypt(message: str, password: str):
    pass


def decrypt(message: str, password: str):
    pass
