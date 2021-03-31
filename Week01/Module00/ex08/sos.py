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
            if char in range(48, 58):
                morse_code += str(morse_number[char - 48][0])
            else:
                morse_code += str(morse_char[char - 65][0])
            j += 1
            if j < llw:
                morse_code += " "
        i += 1
        if i < ll:
            morse_code += " / "
    print(morse_code)
