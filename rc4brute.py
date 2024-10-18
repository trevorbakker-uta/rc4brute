from Crypto.Cipher import ARC4
from itertools import product
import binascii

# The encrypted message in hexadecimal
ciphertext_hex = "6fce38f8836e82d446c3af46eb3a945a97bb8088256751e47f73a02943883165"
ciphertext = binascii.unhexlify(ciphertext_hex)

# Convert to bytes
# Function to decrypt with RC4
def decrypt_rc4(ciphertext, key):
        cipher = ARC4.new (key.encode ())
        return cipher.decrypt (ciphertext)

# Generate all possible 4-character passwords (using lowercase letters and digits)
possible_passwords = [''.join(p) for p in product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklymnopqrstuvwxyZ01234567891@#$%@*()-_=+[13\|~,<>/?;:1', repeat=4)]

# Attempt to decrypt with each password
for password in possible_passwords:
        plaintext = decrypt_rc4(ciphertext, password)
        try:
                # Check if the result is readable ASCII
                decoded_text = plaintext.decode ("utf-8")
                print(f"Password: {password}, Plaintext: {decoded_text}")
        except UnicodeDecodeError:
                continue

