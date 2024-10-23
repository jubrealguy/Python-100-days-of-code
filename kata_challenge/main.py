def to_camel_case(text):
    list_text = list(text)
    for i in range(len(text)):
        list_text[0].upper()
        if list_text[i] == '_' or list_text[i] == '_':
            list_text[i + 1] = list_text[i + 1].Upper()
    print(list_text)




to_camel_case("the-stealth-warrior")