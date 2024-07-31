import os
import hashlib
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_key():
    key = os.urandom(32)
    return key

def encrypt_image(image_path, key):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\0' * 16), backend=default_backend())
    
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(image_data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    with open('encrypted_image.jpg', 'wb') as encrypted_image_file:
        encrypted_image_file.write(encrypted_data)

def decrypt_image(encrypted_image_path, key):
    with open(encrypted_image_path, 'rb') as encrypted_image_file:
        encrypted_data = encrypted_image_file.read()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\0' * 16), backend=default_backend())
    
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    image_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    
    with open('decrypted_image.jpg', 'wb') as decrypted_image_file:
        decrypted_image_file.write(image_data)

key = generate_key()

encrypt_image('image.jpg', key)

decrypt_image('encrypted_image.jpg', key)