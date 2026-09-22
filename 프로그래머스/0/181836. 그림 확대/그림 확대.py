def solution(picture, k):
    answer = []
    for row in picture:
        expanded_row = ""
        for char in row:
            expanded_row += char * k
        for _ in range(k):
            answer.append(expanded_row)
    return answer
