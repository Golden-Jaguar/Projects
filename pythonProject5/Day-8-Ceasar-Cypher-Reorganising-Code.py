import ceasarart


while True:
    print(ceasarart.logo)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def ceasar(cipher_direction, start_text, shift_amount):
        cipher_text = ""
        for letter in start_text:
            if str.isalpha(letter) == True:
                index = alphabet.index(letter)
                if shift_amount > 26:
                    shift_amount = shift_amount % 26
                if cipher_direction == "decode":
                    shift_amount = -abs(shift_amount)
                index += shift_amount
                cipher_text += alphabet[index]
            else:
                cipher_text += letter

        print(f"The {cipher_direction}d text is {''.join(cipher_text)}")


    ceasar(cipher_direction=direction, start_text=text, shift_amount=shift)
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break


