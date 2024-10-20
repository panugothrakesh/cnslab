from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Constants
SECRET_KEY = "my_super_secret_key_ho_ho_ho"
SALT = b"ssshhhhhhhhhhh!!!!"

def encrypt(plain_text):
    # Generate a random IV
    iv = os.urandom(16)
    
    # Derive the key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=65536,
        backend=default_backend()
    )
    key = kdf.derive(SECRET_KEY.encode())

    # Create Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad the plain text to make it a multiple of the block size
    padding_length = 16 - (len(plain_text) % 16)
    padded_plain_text = plain_text + (chr(padding_length) * padding_length)

    # Encrypt the padded plain text
    encrypted = encryptor.update(padded_plain_text.encode()) + encryptor.finalize()
    
    # Return IV + encrypted text (base64 encoded)
    return base64.b64encode(iv + encrypted).decode()

def decrypt(encrypted_text):
    # Decode the base64 encoded text
    encrypted_bytes = base64.b64decode(encrypted_text)
    
    # Extract the IV from the first 16 bytes
    iv = encrypted_bytes[:16]
    encrypted_message = encrypted_bytes[16:]

    # Derive the key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=65536,
        backend=default_backend()
    )
    key = kdf.derive(SECRET_KEY.encode())

    # Create Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the message
    padded_plain_text = decryptor.update(encrypted_message) + decryptor.finalize()
    
    # Unpad the decrypted text
    padding_length = padded_plain_text[-1]
    return padded_plain_text[:-padding_length].decode()

# Driver code
if __name__ == "__main__":
    original_string = "GeeksforGeeks"
    
    # Call encryption method
    encrypted_string = encrypt(original_string)
    
    # Call decryption method
    decrypted_string = decrypt(encrypted_string)

    # Print all strings
    print("Original String: ", original_string)
    print("Encrypted String: ", encrypted_string)
    print("Decrypted String: ", decrypted_string)