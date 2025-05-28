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
Fully reusable VigenereCipher class

Works with any custom alphabet (e.g. lowercase, uppercase, symbols)

Preserves non-alphabet characters as-is

Key is repeated to match the full length of the input (no skipping non-alphabet characters)

## ▶️ How to Run:

```python vigenere_cipher_cli.py```
### 🖥️ Sample Session:

```
Enter do you want to quit? (yes/no): no
"e" for encryption and "d" for decryption: e
Enter messege you want to encrypt: My name is Alex Dhami and I am From {country}
Enter the key: diddy's huge D
Your encrypted messege is :2cdS[tY Rig'l*]i)M[t] JdLeIDFWd+lva dYW[n9Wcb
Enter do you want to quit? (yes/no): no
"e" for encryption and "d" for decryption: d
Enter Encrypted word: 2cdS[tY Rig'l*]i)M[t] JdLeIDFWd+lva dYW[n9Wcb
Enter the key: diddy's huge D
Your plain text messege is : My name is Alex Dhami and I am From {country}
Enter do you want to quit? (yes/no): yes  
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

## 🧠 Vigenère Cipher Summary
The Vigenère Cipher is a method of encrypting text by applying a series of Caesar ciphers based on a keyword. It creates a polyalphabetic substitution system that is much harder to break than a regular Caesar cipher.

# 🛠️ Author
Created with 🧠 by ``Alex Dhami``

