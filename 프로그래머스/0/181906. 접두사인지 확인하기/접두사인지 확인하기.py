def solution(my_string, is_prefix):
    if my_string.startswith(is_prefix):
        return 1
    else:
        return 0
# startswith = 문자열 함수 사용자가 지정한 특정 문자로 시작하는지 확인하는 함수