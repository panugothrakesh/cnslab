import base64

class SimpleDES:
    def __init__(self):
        self.key = "ThisIsSecretEncryptionKey"  # Placeholder for the key (not secure)

    def encrypt(self, unencrypted_string):
        # Simple XOR-based "encryption" for demonstration purposes
        encrypted_bytes = bytearray()
        for i in range(len(unencrypted_string)):
            encrypted_bytes.append(ord(unencrypted_string[i]) ^ ord(self.key[i % len(self.key)]))
        encrypted_string = base64.b64encode(encrypted_bytes).decode('utf-8')
        return encrypted_string

    def decrypt(self, encrypted_string):
        encrypted_bytes = base64.b64decode(encrypted_string)
        decrypted_bytes = bytearray()
        for i in range(len(encrypted_bytes)):
            decrypted_bytes.append(encrypted_bytes[i] ^ ord(self.key[i % len(self.key)]))
        return decrypted_bytes.decode('utf-8')

# Main function to use the SimpleDES class
if __name__ == "__main__":
    des = SimpleDES()
    string_to_encrypt = input("Enter the string to encrypt: ")

    encrypted = des.encrypt(string_to_encrypt)
    decrypted = des.decrypt(encrypted)

    print(f"\nString To Encrypt: {string_to_encrypt}")
    print(f"Encrypted Value: {encrypted}")
    print(f"Decrypted Value: {decrypted}")
