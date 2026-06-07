def caesar(direction, code_text, shift_jumps):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if direction == "encode":
        count_letters = len(code_text)
        jumps = shift_jumps
        output_text = ""
      
        for letter in range(count_letters):
            #if type(int(code_text[letter])) == 'str':
                pos = 0          
                if code_text[letter] in alphabet:
                    #if code_text[letter]:
                    pos = alphabet.index(code_text[letter]) + jumps                
                    if pos > (len(alphabet)-1):
                        pos = pos - len(alphabet)
                        output_text += alphabet[pos]
                else:
                        output_text += code_text[letter]
                  
        print(f"The encrypted code is: {output_text}")
      
    elif direction=="decode":
        count_letters = len(code_text)
        jumps = shift_jumps
        output=""
      
      for letter in range(count_letters):
            pos=0        
            if code_text[letter] in alphabet:
                pos=alphabet.index(code_text[letter])-jumps
                output += alphabet[pos]
            else:
                output += code_text[letter]
              
        print(f"The decrypter code is: {output}")
    else:
            print("Non recognizable parameter")
