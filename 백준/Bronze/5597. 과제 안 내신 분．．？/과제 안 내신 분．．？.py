stu = [i for i in range(1, 31)]
sub = [int(input()) for _ in range(28)]
mis = sorted(set(stu) - set(sub))
for m in mis:
    print(m)