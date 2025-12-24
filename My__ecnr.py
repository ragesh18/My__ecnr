# My__ecnr.py
# Simple Substitution Cipher (Encode & Decode)

# Mapping of letters to symbols
cipher_map = {
    'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&',
    'F': '!', 'G': '^', 'H': '*', 'I': '(', 'J': ')',
    'K': '-', 'L': '}', 'M': '{', 'N': '[', 'O': ']',
    'P': ':', 'Q': ';', 'R': '/', 'S': '?', 'T': '+',
    'U': '=', 'V': '<', 'W': '>', 'X': '×', 'Y': '₹',
    'Z': '±'
}

# Reverse mapping for decoding
reverse_cipher_map = {v: k for k, v in cipher_map.items()}


def encode_message(message):
    """Convert plain text into encoded symbols"""
    encoded = ""
    for char in message.upper():
        if char in cipher_map:
            encoded += cipher_map[char]
        else:
            encoded += char  # keep spaces and symbols unchanged
    return encoded


def decode_message(message):
    """Convert encoded symbols back into plain text"""
    decoded = ""
    for char in message:
        if char in reverse_cipher_map:
            decoded += reverse_cipher_map[char]
        else:
            decoded += char
    return decoded


def main():
    print("🔐 Substitution Cipher (Encode & Decode)")
    print("=" * 40)
    print("1. Encode Message")
    print("2. Decode Message")

    choice = input("Choose an option (1/2): ")

    if choice == "1":
        msg = input("Enter the Message: ")
        print("Plain:", msg)
        print("Encrypted:", encode_message(msg))

    elif choice == "2":
        msg = input("Enter the Encrypted Message: ")
        print("Encrypted:", msg)
        print("Decrypted:", decode_message(msg))

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()

