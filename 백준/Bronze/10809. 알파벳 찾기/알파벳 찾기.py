n = input()

for i in range(26):
    ch = chr(ord('a') + i)
    print(n.find(ch), end=' ')