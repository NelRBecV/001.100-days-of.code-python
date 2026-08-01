from caesar_cipher import caesar
from art_logo import logo

print(logo.main_logo)

answer = "yes"

while answer == "yes":
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shifts = int(input("Type the shift number:\n"))

    print("\nPlease wait for a moment...")

    caesar(operation, message, shifts)
    answer = input("\nDo you want to encode/decode something else?: ").lower()

print("Goodbye")
