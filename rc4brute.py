# Copyright (C) 2024 Trevor Bakker
#
# rc4brute.py free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from Crypto.Cipher import ARC4
from itertools import product
import binascii

# The encrypted message in hexadecimal
ciphertext_hex = ""
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

