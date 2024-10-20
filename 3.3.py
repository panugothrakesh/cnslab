import numpy as np

# Define the matrix size
N = 3

# Function to encrypt the message using the key matrix
def encrypt(key, item):
    # Convert the key string into a matrix
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape(N, N)

    # Convert the item string to a vector
    item_matrix = np.array([ord(char) - ord('A') for char in item])

    # Multiply the key matrix by the item matrix and perform modulo 26
    encrypted_matrix = np.dot(key_matrix, item_matrix) % 26

    # Convert encrypted matrix back to characters
    encrypted_message = ''.join(chr(int(num) + ord('A')) for num in encrypted_matrix)
    
    return encrypted_message

# Function to decrypt the encrypted matrix using the inverse key matrix
def decrypt(inverse_key_matrix, encrypted_message):
    # Convert the encrypted message to a vector
    encrypted_matrix = np.array([ord(char) - ord('A') for char in encrypted_message])

    # Multiply the inverse key matrix by the encrypted matrix and perform modulo 26
    decrypted_matrix = np.dot(inverse_key_matrix, encrypted_matrix) % 26

    # Convert decrypted matrix back to characters
    decrypted_message = ''.join(chr(int(num) + ord('A')) for num in decrypted_matrix)
    
    return decrypted_message

# Main execution
if __name__ == "__main__":
    key = "GYBNQKURP"  # Key for the Hill Cipher (3x3 matrix)
    item = "ACT"       # Message to be encrypted (must have a length of N)

    # Encrypt the message
    encrypted_message = encrypt(key, item)
    print(f"Encrypted Message: {encrypted_message}")

    # Inverse key matrix for decryption (Pre-calculated inverse of key_matrix mod 26)
    inverse_key_matrix = np.array([
        [8, 5, 10],
        [21, 8, 21],
        [21, 12, 8]
    ])

    # Decrypt the message
    decrypted_message = decrypt(inverse_key_matrix, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")