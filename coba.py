def fhash(s, tabsize):
    x = 0
    for c in s:
        x += ord(c)
    return x % tabsize

print(fhash('Rivai', 10))