def convert_letters_to_numbers(input_string,alphabet, numerals, offset):
    input_string=input_string.lower()
    ##print(input_string)
    numeric_output=[]
    #for each character in the message, if it is a letter, change it
    #to the corresponding number and offset it,
    #if not, leave it alone. Returns list of numeric equivalents.
    for j in range(len(input_string)):
        #print(input_string[j])
        #print(input_string[j].isalpha())
        if input_string[j].isalpha():
            alpha_index=alphabet.find(input_string[j])
            numeric_output+=[str((numerals[alpha_index]+offset)%len(alphabet))]
        else:
            numeric_output+=[input_string[j]]
    print (numeric_output)
    return numeric_output

def check_capitalization(decoded_message, input_string):
    if len(decoded_message)==len(input_string):
        new_string=''
        for i in range(len(decoded_message)):
            if input_string[i].isupper():
                new_string=new_string+decoded_message[i].swapcase()
            else:
                new_string=new_string+decoded_message[i]
        return new_string
        
def decode_message(input_string,alphabet, numerals, offset):
    number_list=convert_letters_to_numbers(input_string,alphabet, numerals, offset)
    for l in range(len(number_list)):
        if number_list[l].isdigit():
            number_list[l]=alphabet[int(number_list[l])]
    decoded_message=''.join(number_list)
    return check_capitalization(decoded_message, input_string)

def generate_offset_alphabet(alphabet, offset):
    offset=offset%len(alphabet)
    alphabet2=alphabet[offset:]+alphabet[0:offset]
    return alphabet2


input_string="map"
offset=2
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet2=generate_offset_alphabet(alphabet,offset)


numerals=[]
for i in range(len(alphabet)):
    numerals=numerals+[i]



print (input_string)
print (decode_message(input_string,alphabet, numerals, offset))

print (input_string.translate(input_string.maketrans(alphabet, alphabet2)))


