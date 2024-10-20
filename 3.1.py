def encrypt_decrypt_message():
    text = input("Enter a message to encrypt: ")
    key = int(input("Enter the key: "))

    # Encrypting the message
    encrypted_text = []
    for ch in text:
        if ch.isalnum():
            if ch.islower():
                encrypted_char = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
            elif ch.isupper():
                encrypted_char = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            elif ch.isdigit():
                encrypted_char = chr((ord(ch) - ord('0') + key) % 10 + ord('0'))
        elif ch == ' ':
            encrypted_char = ch  # Preserve space characters
        else:
            print("Invalid Message: Only alphanumeric characters and spaces are allowed")
            return
        encrypted_text.append(encrypted_char)

    encrypted_text = ''.join(encrypted_text)
    print("Encrypted message:", encrypted_text)

    # Decrypting the message
    decrypted_text = []
    for ch in encrypted_text:
        if ch.isalnum():
            if ch.islower():
                decrypted_char = chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
            elif ch.isupper():
                decrypted_char = chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
            elif ch.isdigit():
                decrypted_char = chr((ord(ch) - ord('0') - key + 10) % 10 + ord('0'))
        elif ch == ' ':
            decrypted_char = ch  # Preserve space characters
        else:
            print("Invalid Message: Only alphanumeric characters and spaces are allowed")
            return
        decrypted_text.append(decrypted_char)

    decrypted_text = ''.join(decrypted_text)
    print("Decrypted message:", decrypted_text)

# Running the function directly
encrypt_decrypt_message()