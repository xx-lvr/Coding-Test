n = int(input())
o = n
c = 0

while True:
    a = n // 10
    b = n % 10
    sum = a + b
    n = (b * 10) + (sum % 10)
    c += 1
    
    if n == o:
        break

print(c)