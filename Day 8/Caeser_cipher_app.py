from Caeser_cipher import caeser
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to end the program:\n").lower()
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caeser(text, shift, direction)
    elif direction == 'exit':
        print('Bye, the program is ending')
        break
    else:
        print('Wrong option try again')
# while True:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to end the program:\n").lower()
#     if direction == 'exit':
#         print('Bye, the program is ending')
#         break
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     if direction == 'encode':
#         encrypt_message(text,shift)
#         count += 1
#         print()
#     elif direction == 'decode':
#         decrypt_message(text,shift)
#         print()
#     else:
#         print('Invalid command, try again ')
#
#     if count > 0 :
#         print(f'Your last shift was: {shift} \n')








