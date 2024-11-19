def rotate_word(word, n):
    rotated = ""
    for char in word:
        if char.isalpha():  
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            new_char = chr(start + (ord(char) - start + n) % 26)
            rotated += new_char
        else:
            rotated += char 
    return rotated

print(rotate_word("cheer", 7))  
print(rotate_word("matheus",8))

