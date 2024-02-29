alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_op = True

def cipher(op, txt, shift):
    new_txt = ""
    for letter in txt:
        pos = alphabets.index(letter)
        if op == 'encode':
            new_pos = pos + shift
            if new_pos > 25:
                a = new_pos % 26
                new_pos = a
    
        elif op == 'decode':
            new_pos = pos - shift
            if new_pos < 0:
                a = new_pos + 26
                new_pos = a % 26
        new_txt += alphabets[new_pos]
    print("Your {}d text is {}".format(op, new_txt))

while is_op:
    operation = input("Type encode to encrypt and type decode to decrypt: ").lower()

    if operation == 'encode' or operation == 'decode':
        is_op = False
    else:
        print("WRONG COMMAND!!! Check instruction well")

text = input("Enter text: ").lower()
shift_num = int(input("Shift number: "))

cipher(op=operation, txt=text, shift=shift_num)