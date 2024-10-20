str_text = "Hello World"
str1 = ""
length = len(str_text)
print("The Plain Text: ", end="")
for i in range(length):
    print(str_text[i], end="")
print("\nThe Cipher Text: ", end="")
for i in range(length):
    str1 += chr(ord(str_text[i]) ^ 0)
    print(str1[i], end="")
print()