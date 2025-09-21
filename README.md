How this solution upholds CIA:

Confidentiality: The message is encrypted using AES, so only someone with the secret key can read it.

Integrity: A SHA-256 hash is computed before and after encryption. If even one bit changes, the hash won’t match, proving tampering.

Availability: The script demonstrates that data can be encrypted, stored/transmitted, and decrypted reliably without loss.

Role of Entropy and Key Generation:

Entropy: Strong randomness is crucial. This project uses os.urandom() to get unpredictable random bytes from the operating system, ensuring secure keys and IVs.

Key Generation: AES requires a secret key. By generating a 256-bit random key, the solution makes brute-force attacks computationally infeasible. A fresh key and IV each run prevents reuse attacks.
