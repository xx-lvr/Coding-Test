def solution(array):
    val = max(array)
    index = array.index(val)
    return [val, index]