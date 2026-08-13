def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return str("김서방은 ") + str(i) + str("에 있다")