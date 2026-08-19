def caesar(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

text = input("Enter message: ")
shift = int(input("Enter shift key: "))
choice = input("Encrypt or Decrypt (E/D): ")
    
if choice.lower() == 'd':
    shift = -shift

print("Result:" , caesar(text , shift))