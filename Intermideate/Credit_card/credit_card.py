import os
import hashlib
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_key():
    key = os.urandom(32)
    return key

def encrypt_credit_card_info(credit_card_info, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\0' * 16), backend=default_backend())

    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(credit_card_info) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    return encrypted_data

def decrypt_credit_card_info(encrypted_data, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\0' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    credit_card_info = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    
    return credit_card_info

key = generate_key()

credit_card_info = "Card Number: 1234-5678-9012-3456, Expiration Date: 12/25, CVV: 123"
encrypted_data = encrypt_credit_card_info(credit_card_info, key)

cloud_storage.store(encrypted_data)

decrypted_data = decrypt_credit_card_info(encrypted_data, key)
print("Decrypted Credit Card Information:", decrypted_data)