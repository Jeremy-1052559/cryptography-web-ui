import base64
import os
import pathlib

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
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


def get_cipher(secret_key: bytes, iv: bytes):
    algo = algorithms.AES256(secret_key)  # Select algorithm and attach secret key
    mode = modes.CBC(iv)  # Select mode and attach initialization vector
    return Cipher(algo, mode)  # Obtain cipher from algorithm and mode


def encrypt(message: str, password: str):
    salt = os.urandom(16)  # Generate unique salt
    iv = os.urandom(16)  # Generate unique initialization vector
    key = get_secret_key(password, salt)  # Generate key from password and random salt
    cipher = get_cipher(key, iv)
    encryptor = cipher.encryptor()  # Obtain new cipher context for encryption
    padder = padding.PKCS7(
        128
    ).padder()  # Obtain new padder to pad content before encryption
    padded = (
        padder.update(message) + padder.finalize()
    )  # Load message into padder and close padder
    cipher_text = (
        encryptor.update(padded) + encryptor.finalize()
    )  # Load padded message into cipher context and close context
    return (
        base64.b64encode(salt + iv + cipher_text).decode()
    )  # Encode salt, vector, and encrypted text to base64 and decode bytes to utf-8


def decrypt(message: str, password: str):
    encrypted = base64.b64decode(message)
    salt = encrypted[:16]  # First 16 chars are the salt
    iv = encrypted[16:32]  # Second 16 chars is the initialization vector
    encrypted = encrypted[32:]  # Rest is the actual encrypted message
    key = get_secret_key(
        password, salt
    )  # If not tampered with, salt should generate the same key
    cipher = get_cipher(key, iv)
    decryptor = cipher.decryptor()  # Obtain new cipher context for decryption
    unpadder = padding.PKCS7(
        128
    ).unpadder()  # Obtain new unpadder to remove padding from content after decryption
    padded = (
        decryptor.update(encrypted) + decryptor.finalize()
    )  # Decrypt message into padded message
    original_text = (
        unpadder.update(padded) + unpadder.finalize()
    )  # Remove padding from message to retrieve original content
    return original_text.decode()  # Decode retrieved content bytes to utf-8
