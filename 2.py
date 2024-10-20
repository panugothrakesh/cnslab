str_text = "Hello World"
str1 = ""
str2 = ""
str3 = ""
length = len(str_text)

# Plain Text
print("The Plain Text: ", end="")
for i in range(length):
    print(str_text[i], end="")

# AND Operation
print("\nCipher text after AND Operation: ", end="")
for i in range(length):
    str1 += chr(ord(str_text[i]) & 127)
    print(str1[i], end="")

# XOR Operation
print("\nCipher text after XOR Operation: ", end="")
for i in range(length):
    str3 += chr(ord(str_text[i]) ^ 127)
    print(str3[i], end="")

# OR Operation
print("\nCipher text after OR Operation: ", end="")
for i in range(length):
    str2 += chr(ord(str_text[i]) | 127)
    print(str2[i], end="")

print()
