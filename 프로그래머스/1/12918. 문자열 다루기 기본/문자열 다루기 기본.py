def solution(s):
    return (len(s) == 4 or len(s) == 6) & s.isdigit()

# isdigit() -> 숫자로만 이루어져있는지 확인하는 메서드