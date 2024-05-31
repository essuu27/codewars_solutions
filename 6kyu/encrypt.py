def decrypt(encrypted_text, n):
    pass

def encrypt(text, n):
    for _ in range(n):
        str1 = ''
        str2 = ''
        for x, y in enumerate(text):
            if x // 2 == x / 2:
                str1 = str1 + str(y)
            else:
                str2 = str2 + str(y)
        text = str1 + str2
    return text

print(encrypt("1234abcd",1))
print(encrypt("1234abcd",2))
print(encrypt("1234abcd",3))
print(encrypt("1234abcd",4))
print(encrypt("1234abcd",5))
print(encrypt("1234abcd",6))
print(encrypt("1234abcd",7))
print(encrypt("1234abcd",8))

