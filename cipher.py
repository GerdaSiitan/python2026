def cipher_text(text, key, direction=1):
    result = ""
    key = key.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_index = 0

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.index(char)
            new_index = (index + direction * offset) % 26
            new_char = alphabet[new_index]
            if is_upper:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result


def encrypt(text, key):
    return cipher_text(text, key, 1)


def decrypt(text, key):
    return cipher_text(text, key, -1)


print("Vali tegevus:")
print("1 - Šifreeri")
print("2 - Dešifreeri")

choice = input("Sisesta valik (1/2): ")
text = input("Sisesta tekst: ")
key = input("Sisesta võti: ")

if choice == "1":
    result = encrypt(text, key)
    print("Šifreeritud tekst:", result)
elif choice == "2":
    result = decrypt(text, key)
    print("Dešifreeritud tekst:", result)
else:
    print("Vale valik!")