SIZE = 5

# Generate key table for Playfair cipher
def generate_key_table(key):
    key_table = []
    used = set()
    for char in key + 'abcdefghiklmnopqrstuvwxyz':  # 'j' is skipped
        if char not in used and char != 'j':
            key_table.append(char)
            used.add(char)
    return [key_table[i:i+SIZE] for i in range(0, len(key_table), SIZE)]

# Search for positions of two characters in the key table
def search(key_table, a, b):
    if a == 'j': 
        a = 'i'
    if b == 'j': 
        b = 'i'
    pos = [divmod(key_table.index(char), SIZE) for char in [a, b]]
    return pos

# Encrypt message
def playfair_cipher(message, key_table, mode='encrypt'):
    result = []
    shift = 1 if mode == 'encrypt' else -1
    message = message.replace('j', 'i')
    if len(message) % 2 != 0:
        message += 'x'
    for i in range(0, len(message), 2):
        a_pos, b_pos = search(key_table, message[i], message[i+1])
        if a_pos[0] == b_pos[0]:  # Same row
            result.append(key_table[a_pos[0] * SIZE + (a_pos[1] + shift) % SIZE])
            result.append(key_table[b_pos[0] * SIZE + (b_pos[1] + shift) % SIZE])
        elif a_pos[1] == b_pos[1]:  # Same column
            result.append(key_table[((a_pos[0] + shift) % SIZE) * SIZE + a_pos[1]])
            result.append(key_table[((b_pos[0] + shift) % SIZE) * SIZE + b_pos[1]])
        else:  # Rectangle swap
            result.append(key_table[a_pos[0] * SIZE + b_pos[1]])
            result.append(key_table[b_pos[0] * SIZE + a_pos[1]])
    return ''.join(result)

# Main
key = input("Enter key (without 'j'): ").replace('j', 'i')
message = input("Enter message (without 'j'): ").replace('j', 'i')
key_table = [item for sublist in generate_key_table(key) for item in sublist]  # Flatten key table

encrypted_message = playfair_cipher(message, key_table, mode='encrypt')
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = playfair_cipher(encrypted_message, key_table, mode='decrypt')
print(f"Decrypted Message: {decrypted_message}")
