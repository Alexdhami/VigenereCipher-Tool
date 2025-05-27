## 🔐 Vigenère Cipher Tool (Python)
This project implements the classic Vigenère cipher in two ways:

A CLI (Command-Line Interface) version for interactive use

A module version (importable class) for programmatic use

## 📁 Files
```vigenere_cipher_cli.py``` — Interactive CLI version

```vigenere_cipher_module.py``` — Importable class version

## 🧪 Requirements
```Python 3.x```

No external dependencies.

## 🚀 Usage
1. 🔸 CLI Version: ```vigenere_cipher_cli.py```
   
### ✅ Features:
Interactive prompt for encryption and decryption

You must provide the key and it assumes only capital letters (A–Z)

Spaces are removed from input for simplicity

Uses a full Vigenère table (26x26 Caesar-shifted rows)

## ▶️ How to Run:

```python vigenere_cipher_cli.py```
### 🖥️ Sample Session:

```
Enter do you want to quit? (yes/no): no
"e" for encryption and "d" for decryption: e
Enter message you want to encrypt: HELLOWORLD
Enter the key: KEY
Your encrypted word RIJVSUYVJN.

Enter do you want to quit? (yes/no): no
"e" for encryption and "d" for decryption: d
Enter Encrypted word: RIJVSUYVJN
Enter the key: KEY
Your plain text message is: HELLOWORLD  
```
2. 🔸 Module Version: ```vigenere_cipher_module.py```

### ✅ Features:
Fully reusable VigenereCipher class

Works with any custom alphabet (e.g. lowercase, uppercase, symbols)

Preserves non-alphabet characters as-is

Key is repeated to match the full length of the input (no skipping non-alphabet characters)

## ▶️ Example Usage:
python
```

from vigenere_cipher_module import VigenereCipher

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "password"

cipher = VigenereCipher(key, alphabet)

encoded = cipher.encode("codewars")
print(encoded)  # Output: rovwsoiv

decoded = cipher.decode(encoded)
print(decoded)  # Output: codewars
```
## 📌 Notes
In the CLI version, only uppercase English letters (A–Z) are supported.

In the module version, any alphabet can be used (e.g. lowercase only, alphanumeric, etc.).

Characters not in the alphabet are left unchanged.

## 🧠 Vigenère Cipher Summary
The Vigenère Cipher is a method of encrypting text by applying a series of Caesar ciphers based on a keyword. It creates a polyalphabetic substitution system that is much harder to break than a regular Caesar cipher.

# 🛠️ Author
Created with 🧠 by ``Alex Dhami``

