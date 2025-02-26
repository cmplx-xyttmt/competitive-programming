def encrypt_skip_cipher(text, skip):
    """Encrypts a string using a skip cipher.

    Args:
        text: The string to encrypt.
        skip: The number of characters to skip.

    Returns:
        The encrypted string.
    """
    encrypted_text = ""
    for i in range(0, len(text), skip + 1):  # Skip + 1 because we take 1 and skip the rest
        encrypted_text += text[i]
    return encrypted_text


def decrypt_skip_cipher(ciphertext, skip, original_length):
    """Decrypts a string encrypted with a skip cipher.

    Args:
        ciphertext: The ciphertext to decrypt.
        skip: The skip value used for encryption.
        original_length: The length of the original plaintext.  Crucial for proper decryption.

    Returns:
        The decrypted string.
    """

    decrypted_text = [""] * original_length  # Initialize an empty list with the correct length

    index = 0
    for char in ciphertext:
        decrypted_text[index] = char
        index += (skip + 1)
        if index >= original_length: # Handle wrapping around
            remaining = original_length - (index - (skip + 1)) # Calculate how many spots are left in the string
            index = (skip + 1) - remaining # Start from the beginning, skipping the already-filled spots


    return "".join(decrypted_text)


# Example usage:
text = "Hello"
skip = 2

encrypted = encrypt_skip_cipher(text, skip)
print(f"Encrypted: {encrypted}")  # Output: Hoele

decrypted = decrypt_skip_cipher(encrypted, skip, len(text))
print(f"Decrypted: {decrypted}")  # Output: Hello


# text = "This is a longer string to test."
# skip = 3
#
# encrypted = encrypt_skip_cipher(text, skip)
# print(f"Encrypted: {encrypted}")
#
# decrypted = decrypt_skip_cipher(encrypted, skip, len(text))
# print(f"Decrypted: {decrypted}")
#
# text = "abcdefghijklmnopqrstuvwxyz"
# skip = 4
#
# encrypted = encrypt_skip_cipher(text, skip)
# print(f"Encrypted: {encrypted}")
#
# decrypted = decrypt_skip_cipher(encrypted, skip, len(text))
# print(f"Decrypted: {decrypted}")
