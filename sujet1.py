def stringUpCase(mystr):
    out = ""
    for ch in mystr:
        if ord (ch) >= 97 and ord(ch) <= 122:
            out = out + chr(ord(ch) - 32)
        else:
            out = out + ch
    return out
