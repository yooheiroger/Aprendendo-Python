# def encrypt_message(message, shift):
#     list_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     list_message = list(message)
#     encrypt = []
#
#     for char in list_message:# scroll through the entire list for each character in list_message
#         if char in list_letter:# if char in the list(have the alphabet)
#             new_index = (list_letter.index(char) + shift) % len(list_letter)# take the index of char and plus shift. % len(list_letter) will guarantee a loop through the list
#                 # % len(list_letter) = if your text have z and your shit is 3 it is out of index range, 26+3 = 29.
#                 # 29 % len(list_letter), will divide de number 29 for 26 and return the rest of the divide = 3, the new index letter "D"
#             encrypt.append(list_letter[new_index])# add the new letter with the new index to de list called encrypt
#         elif char == ' ':# if the message has spaces, this way will guarantee the spaces in the message
#             encrypt.append(' ')
#         else:
#             print('You type something different than a letter')
#     encrypted_message = ''.join(encrypt)
#     print(f'Your encoded text is: {encrypted_message}')
#
# def decrypt_message(message,shift):
#     list_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                    'u', 'v', 'w', 'x', 'y', 'z']
#     list_message = list(message)
#     decrypt = []
#     for char in list_message: # scroll through the entire list for each character in list_message
#         if char in list_letter:# if char in the list(have the alphabet)
#             new_index = (list_letter.index(char) - shift) % len(list_letter) # take the index of char and minus shift. % len(list_letter) will guarantee a loop through the list
#             decrypt.append(list_letter[new_index]) # add the new letter with the new index to de list called decrypt
#         elif char == ' ':# if the message has spaces, this way will guarantee the spaces in the message
#             decrypt.append(' ')
#         else:
#             print('You type something different than a letter')
#     message_decrypted = ''.join(decrypt)
#     print(f'You decoded message is : {message_decrypted}')
#
#
#

# Join the 2 function in One
def caeser(message,  shift, encode_or_decode):
    if encode_or_decode == 'decode':
        shift *=-1
    list_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_message = list(message)
    encrypt = []
    for char in list_message:  # scroll through the entire list for each character in list_message
        if char not in list_letter:
            encrypt.append(char)
        if char in list_letter:  # if char in the list(have the alphabet)
            new_index = (list_letter.index(char) + shift) % len(
                list_letter)  # take the index of char and plus shift. % len(list_letter) will guarantee a loop through the list
            # % len(list_letter) = if your text have z and your shit is 3 it is out of index range, 26+3 = 29.
            # 29 % len(list_letter), will divide de number 29 for 26 and return the rest of the divide = 3, the new index letter "D"
            encrypt.append(list_letter[new_index])  # add the new letter with the new index to de list called encrypt
        # elif char == ' ':  # if the message has spaces, this way will guarantee the spaces in the message
        #     encrypt.append(' ')
    encrypted_message = ''.join(encrypt)
    print(f'Your encoded text is: {encrypted_message}')




