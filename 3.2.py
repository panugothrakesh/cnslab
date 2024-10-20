def encrypt(message, key):
    encrypted_message = []
    for char in message:
        if 'a' <= char <= 'z':  # Check if it's a lowercase letter
            encrypted_message.append(key[ord(char) - ord('a')])
        else:
            encrypted_message.append(char)  # Leave non-lowercase characters unchanged
    return ''.join(encrypted_message)

def decrypt(message, key):
    decrypted_message = []
    for char in message:
        if char in key:
            decrypted_message.append(chr(key.index(char) + ord('a')))
        else:
            decrypted_message.append(char)  # Leave non-lowercase characters unchanged
    return ''.join(decrypted_message)

# Input the substitution key
key = input("Enter the substitution key (26 lowercase letters in random order): ")

# Validate key length
if len(key) != 26:
    print("Invalid key length. Please provide 26 letters.")
    exit(1)

# Validate key characters
if not all('a' <= char <= 'z' for char in key):
    print("Invalid key. Please provide only lowercase letters.")
    exit(1)

# Input the message
message = input("Enter the message to encrypt: ")

# Encrypt the message
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
