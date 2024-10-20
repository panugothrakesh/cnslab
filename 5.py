from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

class SimpleBlowfish:
    def __init__(self, key):
        # Ensure key is between 4 and 56 bytes
        self.key = key
        self.bs = Blowfish.block_size  # Block size for Blowfish (8 bytes)

    def encrypt(self, plaintext):
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        padded_data = pad(plaintext.encode('utf-8'), self.bs)
        encrypted_bytes = cipher.encrypt(padded_data)
        encrypted_string = base64.b64encode(encrypted_bytes).decode('utf-8')
        return encrypted_string

    def decrypt(self, encrypted_string):
        encrypted_bytes = base64.b64decode(encrypted_string)
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        decrypted_padded = cipher.decrypt(encrypted_bytes)
        return unpad(decrypted_padded, self.bs).decode('utf-8')

# Main function to use the SimpleBlowfish class
if __name__ == "__main__":
    # Example key (must be between 4 and 56 bytes)
    key = b'SimpleKey12345'

    blowfish = SimpleBlowfish(key)

    # Input string to encrypt
    string_to_encrypt = input("Enter the string to encrypt: ")

    # Encrypt the input string
    encrypted = blowfish.encrypt(string_to_encrypt)
    print(f"Encrypted Value: {encrypted}")

    # Decrypt the encrypted string
    decrypted = blowfish.decrypt(encrypted)
    print(f"Decrypted Value: {decrypted}")