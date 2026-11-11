# Caesar Cipher CLI

A lightweight, zero-dependency Python command-line tool to encrypt, decrypt, and brute-force crack Caesar Cipher messages.

## Features
* **Encrypt & Decrypt:** Shift letters using any custom key (1–25) while keeping spaces, numbers, and punctuation intact.
* **Brute-Force Cracker:** Automatically test all 25 possible alphabet shifts to unlock an unknown message without the key.
* **Zero Dependencies:** Uses only Python's built-in standard library.

## Usage

### Encrypt a Message
```bash
python caesar.py encrypt "Meet at the secret base" -k 7
```
**Output:** `Tlla ha aol zljyla ihzl`

### Decrypt a Message
```bash
python caesar.py decrypt "Tlla ha aol zljyla ihzl" -k 7
```
**Output:** `Meet at the secret base`

### Crack an Unknown Code
```bash
python caesar.py crack "Tlla ha aol zljyla ihzl"
```

## Disclaimer
This project is built strictly for educational purposes, puzzles, and learning the basics of classical cryptography. Because the Caesar Cipher only has 25 possible shift keys, it offers zero real-world security and can be cracked in milliseconds (as shown by the built-in `crack` mode). **Do not use this tool to protect passwords, personal data, or sensitive information.**

## License
This project is licensed under the MIT License.
