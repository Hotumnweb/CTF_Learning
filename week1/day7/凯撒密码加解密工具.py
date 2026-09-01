def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                # 大写字母：A=65
                start = ord('A')  # 65
                offset = (ord(ch) - start + shift) % 26
                new_ch = chr(start + offset)
            else:
                # 小写字母：a=97
                start = ord('a')  # 97
                offset = (ord(ch) - start + shift) % 26
                new_ch = chr(start + offset)
            result += new_ch
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    # 解密：反向位移，shift 取负数
    return caesar_encrypt(text, -shift)


# 测试
encrypted = caesar_encrypt("flag{caesar_cipher}", 3)
print(encrypted)  # iodj{fdhvdu_flskhu}

decrypted = caesar_decrypt(encrypted, 3)
print(decrypted)  # flag{caesar_cipher}