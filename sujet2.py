def div3(x):
    if x in[0, 3, 6, 9]:
        return True
    if x < 10:
        return False
    add = 0
    for n in str(x):
        add = add + int(n)
    div3(add)
