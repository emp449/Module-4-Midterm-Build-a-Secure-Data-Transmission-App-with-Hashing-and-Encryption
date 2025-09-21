import hashlib
import base64
import os

# --- Helper functions ---
def sha256_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def simple_encrypt(data: bytes, key: bytes) -> bytes:
    # XOR each byte with key (very simple, not secure like AES)
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def simple_decrypt(data: bytes, key: bytes) -> bytes:
    # XOR again to decrypt
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# --- Main Program ---
if __name__ == "__main__":
    # 1. User input
    user_input = input("Enter a message: ").encode()

    # 2. Hash input
    original_hash = sha256_hash(user_input)
    print("Original SHA-256 Hash:", original_hash)

    # 3. Generate random key
    key = os.urandom(16)

    # 4. Encrypt input
    ciphertext = simple_encrypt(user_input, key)
    print("Encrypted (base64):", base64.b64encode(ciphertext).decode())

    # 5. Decrypt and verify
    decrypted = simple_decrypt(ciphertext, key)
    decrypted_hash = sha256_hash(decrypted)

    print("Decrypted Message:", decrypted.decode())
    print("Decrypted SHA-256 Hash:", decrypted_hash)

    if original_hash == decrypted_hash:
        print("✅ Integrity Verified: Hashes match.")
    else:
        print("❌ Integrity Failed: Hash mismatch.")
