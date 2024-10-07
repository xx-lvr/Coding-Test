## 문제 이해⭐
+ 주어진 문자열 rny_string에서 모든 문자 'm'을 'rn'으로 대체하는 문제

## 문제 풀이👍
+ 문자열에서 특정 문자를 다른 문자로 대체하기 위해 replace() 메서드를 사용한다.
+ replace(/m/g, 'rn')는 정규식을 사용하여 문자열의 모든 'm'을 'rn'으로 변경한다.
## 코드 설명
```javascript
function solution(rny_string) {
    return rny_string.replace(/m/g, 'rn'); // 'm'을 'rn'으로 대체
}
```
+ /m/g는 정규식으로 'm'이라는 문자를 찾으며, g 플래그는 전역 검색을 의미한다. 즉, 문자열 내의 모든 'm'을 찾는다.
+ replace() 메서드는 일치하는 'm'을 'rn'으로 대체한다.
