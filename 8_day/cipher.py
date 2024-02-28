def cipher(alpha, op, txt, shift):
    new_txt = ""
    if op == 'encode':
        for letter in txt:
            pos = alpha.index(letter)
            new_pos = pos + shift
            if new_pos > 25:
                new_pos -= 26
            new_txt += alpha[new_pos]
        print("Your encrypted text is {}".format(new_txt))
    
    elif op == 'decode':
        for letter in txt:
            pos = alpha.index(letter)
            new_pos = pos - shift
            if new_pos < 0:
                new_pos += 26
            new_txt += alpha[new_pos]
        print("Your decrypted text is {}".format(new_txt))
    else:
        print("wrong command")
    

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
operation = input("Type encode to encrypt and type decode to decrypt: ").lower()
text = input("Enter text: ").lower()
shift_num = int(input("Shift number: "))

cipher(alpha=alphabets, op=operation, txt=text, shift=shift_num)