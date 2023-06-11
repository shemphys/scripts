import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import getpass

def encrypt_file(key, file_path, output_path):
    print(f"Inside encrypt_file with file_path = {file_path} and output_path = {output_path}")
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(output_path, 'wb') as f:
        f.write(encrypted)

def encrypt_folder(key, folder_path, output_folder):
    print(f"Inside encrypt_folder with folder_path = {folder_path} and output_folder = {output_folder}")
    for foldername, subfolders, filenames in os.walk(folder_path):
        print(f"Folder: {foldername}, Subfolders: {subfolders}, Files: {filenames}")
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            rel_path = os.path.relpath(foldername, folder_path)
            if rel_path == ".":
                rel_path = ""
            output_path_folder = os.path.join(output_folder, rel_path)
            os.makedirs(output_path_folder, exist_ok=True)
            output_path = os.path.join(output_path_folder, f"{filename}.enc")
            print(f"Encrypting {file_path} to {output_path}")
            encrypt_file(key, file_path, output_path)

# Derive a secure symmetric key from a password
password_provided = getpass.getpass("Please enter a password: ")  # This should be replaced with a prompt to the user
password = password_provided.encode()  # Convert to type bytes
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

folder_path = "C:/Users/mykje/Documents/GitHub/scripts/cypher/notcypheredfolder"
output_folder = "C:/Users/mykje/Documents/GitHub/scripts/cypher/cyphered"

print(f"folder_path = {folder_path}, output_folder = {output_folder}")
encrypt_folder(key, folder_path, output_folder)

# Save the salt, you will need it to recreate the key for decryption
with open('salt.txt', 'wb') as f:
    f.write(salt)
