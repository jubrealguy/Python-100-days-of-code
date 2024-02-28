def cipher(alpha, op, txt, shift):
    if op == 'encode':
        txt_list = list(txt)
        new_list = []
        i = 0
        while i < len(txt_list):
            for j in range(len(alphabets)):
                if txt_list[i] == alpha[j]:
                    new_list.append(alpha[j + shift])
                    i += 1
                    break
        
    elif op == 'decode':
        for i, j in zip(range(len(txt_list)), range(len(alpha))):
            if txt_list[i] == alpha[j]:
                txt_list[i] = alpha[j - shift]
    txt_str = ''.join(new_list)
    print(txt_str)
    

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
operation = input("Type encode to encrypt and type decode to decrypt: ")
text = input("Enter text: ")
shift_num = int(input("Shif number: "))

cipher(alpha=alphabets, op=operation, txt=text, shift=shift_num)