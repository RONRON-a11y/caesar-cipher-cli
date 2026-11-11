import argparse
import string

def caesar_shift(text: str, shift: int, decrypt: bool = False) -> str:
    """Shifts letters by the given key while preserving spaces, numbers, and symbols."""
    if decrypt:
        shift = -shift
    
    # Keep the shift within 0-25
    shift = shift % 26
    result = []

    for char in text:
        if char in string.ascii_uppercase:
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(shifted))
        elif char in string.ascii_lowercase:
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(shifted))
        else:
            # Keep punctuation, spaces, and numbers unchanged
            result.append(char)

    return "".join(result)

def brute_force(text: str) -> None:
    """Prints all 25 possible shifts to crack a message without the key."""
    print("\n--- Brute-Force Results ---")
    for key in range(1, 26):
        attempt = caesar_shift(text, key, decrypt=True)
        print(f"Key {key:02d}: {attempt}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caesar Cipher CLI Encryption & Cracker Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt", "crack"], help="Action to perform")
    parser.add_argument("text", help="The message or encrypted code")
    parser.add_argument("-k", "--key", type=int, default=3, help="Shift key (1-25, default: 3)")
    
    args = parser.parse_args()

    if args.mode == "encrypt":
        print(f"\nEncrypted (Key {args.key}):\n{caesar_shift(args.text, args.key)}")
    elif args.mode == "decrypt":
        print(f"\nDecrypted (Key {args.key}):\n{caesar_shift(args.text, args.key, decrypt=True)}")
    elif args.mode == "crack":
        brute_force(args.text)
