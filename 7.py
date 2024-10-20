def swap(a, b):
    return b, a

def KSA(key):
    S = list(range(256))
    keylen = len(key)
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % keylen]) % 256
        S[i], S[j] = swap(S[i], S[j])
    
    return S

def PRGA(S, data):
    i = j = 0
    output = []

    for k in range(len(data)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = swap(S[i], S[j])
        output.append(data[k] ^ S[(S[i] + S[j]) % 256])
    
    return output

def rc4(key, data):
    S = KSA(key)
    return PRGA(S, data)

if __name__ == "__main__":
    # Asking for user input
    key_input = input("Enter the key: ")
    plaintext_input = input("Enter the plaintext: ")

    key = [ord(c) for c in key_input]
    plaintext = [ord(c) for c in plaintext_input]

    # Encrypt the plaintext
    ciphertext = rc4(key, plaintext)
    print("Ciphertext: ", ' '.join(f"{byte:02X}" for byte in ciphertext))

    # Decrypt the ciphertext
    decryptedtext = rc4(key, ciphertext)
    decryptedtext_str = ''.join(chr(byte) for byte in decryptedtext)
    print("Decrypted Text: ", decryptedtext_str)
