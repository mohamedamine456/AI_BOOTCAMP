import sys

if len(sys.argv) > 0:
    morse_char = [[".-"], ["-..."], ["-.-."], ["-.."], ["."], ["..-."], ["--."],
                  ["...."], [".."], [".---"], ["-.-"], [".-.."], ["--"], ["-."], ["---"],
                  [".--."], ["--.-"], [".-."], ["..."], ["-"], ["..-"], ["...-"], [".--"],
                  ["-..-"], ["-.--"], ["--.."]]
    morse_number = [["-----"], [".----"], ["..---"], ["...--"], ["....-"],
                    ["....."], ["-...."], ["--..."], ["---.."], ["----."]]

    all_words = [word.upper() for i in range(1, len(sys.argv)) for word in sys.argv[i].split()]

    if all(word.isalnum() for word in all_words):
        morse_code = " / ".join([" ".join([morse_number[ord(char) - 48][0] if char.isdigit() else morse_char[ord(char) - 65][0] for char in word]) for word in all_words])
        if morse_code != "":
            print(morse_code)
    else:
        print("ERROR")
else:
    print("ERROR")
