import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import getpass

def decrypt_file(key, file_path, output_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(output_path, 'wb') as f:
        f.write(decrypted)

def decrypt_folder(key, folder_path, output_folder):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            rel_path = os.path.relpath(foldername, folder_path)
            if rel_path == ".":
                rel_path = ""
            output_path_folder = os.path.join(output_folder, rel_path)
            os.makedirs(output_path_folder, exist_ok=True)
            if filename.endswith('.enc'):  # Only try to decrypt files that were encrypted
                output_path = os.path.join(output_path_folder, filename[:-4])  # Remove the .enc from the filename
                print(f"Decrypting {file_path} to {output_path}")
                decrypt_file(key, file_path, output_path)

# Derive a secure symmetric key from a password
password_provided = getpass.getpass("Please enter the password that was used for encryption: ")
password = password_provided.encode()  # Convert to type bytes
salt = open('salt.txt', 'rb').read()  # Read the salt that was used for encryption
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

folder_path = "C:/Users/mykje/Documents/GitHub/scripts/cypher/cyphered"
output_folder = "C:/Users/mykje/Documents/GitHub/scripts/cypher/decyphered"

decrypt_folder(key, folder_path, output_folder)
