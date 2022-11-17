n = int(input())
a = [1]
while len(a) < n:
    f = sum(a[-2:])
    print(f)
    a.append(f)
print(*a)

bash: cd: too many arguments
