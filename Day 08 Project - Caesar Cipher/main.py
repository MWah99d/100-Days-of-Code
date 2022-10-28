from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(input_text, shift_amount, process_direction):
    cipher_text = ""
    if process_direction == "decode":
        shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            new_index = alphabet.index(char) + shift_amount
            cipher_text += alphabet[new_index]
        else:
            cipher_text += char
    print(f"The {process_direction}d text is {cipher_text}")


print(logo)
new_process = True
while new_process:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    caesar(text, shift, direction)

    restart = input("Do you want to restart the program? ").lower()
    if restart == "no":
        new_process = False
        print("Goodbye")
