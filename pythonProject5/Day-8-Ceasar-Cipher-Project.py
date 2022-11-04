alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    print(f"Shift = {shift}")
    print(f"Plain_text = {plain_text}.")
    text_list = list(plain_text)
    cipher_text = ""
    for letter1 in text_list:
        for letter in alphabet:
            if letter1 == letter:
                index = alphabet.index(letter)
                index += shift_amount
                if index > 26:
                    index = index - 26
                    cipher_text += alphabet[index]
                else:
                    cipher_text += alphabet[index]

    print(f"The encoded text is {''.join(cipher_text)}")

def decrypt(plain_text, shift_amount):
    print(f"Shift = {shift}")
    print(f"Plain_text = {plain_text}.")
    text_list = list(plain_text)
    cipher_text = ""
    for letter1 in text_list:
        for letter in alphabet:
            if letter1 == letter:
                index = alphabet.index(letter)
                index -= shift_amount
                if index > 26:
                    index = index - 26
                    cipher_text += alphabet[index]
                else:
                    cipher_text += alphabet[index]

    print(f"The encoded text is {''.join(cipher_text)}")




if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(plain_text=text, shift_amount=shift)