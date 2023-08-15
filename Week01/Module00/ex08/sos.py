import sys

if len(sys.argv) > 1:
    morse_char = [[".-"], ["-..."], ["-.-."], ["-.."], ["."], ["..-."], ["--."],
            ["...."], [".."], [".---"], ["-.-"], [".-.."], ["--"], ["-."], ["---"],
            [".--."], ["--.-"], [".-."], ["..."], ["-"], ["..-"], ["...-"], [".--"],
            ["-..-"], ["-.--"], ["--.."]]
    morse_number = [["-----"], [".----"], ["..---"], ["...--"], ["....-"],
            ["....."], ["-...."], ["--..."], ["---.."], ["----."]]
    
    i = 1
    all_words = []
    while i < len(sys.argv):
        tab_word = sys.argv[i].split()
        for word in tab_word:
            if word.isalnum() == False:
                print("ERROR")
                exit()
            else:
                all_words.append(word.upper())
        i += 1
    i = 0
    morse_code = ""
    ll = len(all_words)
    while i < ll:
        llw = len(all_words[i])
        j = 0
        while j < llw:
            char = ord(all_words[i][j])
            morse_code += [str(morse_number[char - 48][0]) if char in range(48, 58) else str(morse_char[char - 65][0])][0]
            j += 1
            morse_code += [" " if j < llw else ""][0]
                
        i += 1
        morse_code += [" / " if i < ll else ""][0]
    print(morse_code)
