def caesar(direction, code_text, shift_jumps):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_length = len(alphabet)
    if direction == "encode":
        count_letters = len(code_text)
        output_text = ""
      
        for letter in range(count_letters):
            if code_text[letter] in alphabet:
                pos = alphabet.index(code_text[letter]) + shift_jumps
                if pos > alphabet_length:
                    jump = pos - (pos // alphabet_length) * alphabet_length
                    pos = jump
                output_text += alphabet[pos]
            else:
                output_text += code_text[letter]
                  
        print(f"The encrypted code is: {output_text}")
      
    elif direction == "decode":
        count_letters = len(code_text)
        output = ""
      
        for letter in range(count_letters):
            if code_text[letter] in alphabet:
                pos = alphabet.index(code_text[letter]) - shift_jumps
                if pos < alphabet_length:
                    jump = pos + (abs(pos) // alphabet_length) * alphabet_length
                    pos = jump
                output += alphabet[pos]
            else:
                output += code_text[letter]
        print(f"The decrypter code is: {output}")
    else:
        print("Non recognizable parameter")
