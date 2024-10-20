import math

def gcd(a, b):
    while b: 
        a, b = b, a % b
    return a

def modpow(a, b, m):
    result = 1
    while b:
        if b % 2:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

def generate_keys(p, q):
    n, phi_n = p * q, (p - 1) * (q - 1)
    e = 3 if phi_n % 3 else 5  # Select a small prime for e
    while gcd(e, phi_n) != 1: 
        e += 2  # Ensure e is coprime with phi(n)
    d = pow(e, -1, phi_n)  # Calculate d using modular inverse
    return (e, n), (d, n)

if __name__ == "__main__":
    p, q = 3,5
    public_key, private_key = generate_keys(p, q)

    m = 11  # Original message
    c = modpow(m, public_key[0], public_key[1])  # Encrypted message
    decrypted = modpow(c, private_key[0], private_key[1])  # Decrypted message

    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")
    print(f"Original message: {m}")
    print(f"Encrypted message: {c}")
    print(f"Decrypted message: {decrypted}")