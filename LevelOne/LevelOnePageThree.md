# 프로그래머스 레벨 1 페이지 3

## 목차
1. [두개뽑아서더하기](#두개뽑아서더하기)
2. [2016](#2016)


## 두개뽑아서더하기
```markdown
정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 
더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.

입출력 예
numbers	     result
[2,1,3,4,1]	[2,3,4,5,6,7]
[5,0,2,7]	[2,5,7,9,12]
```
```typescript
function solution(numbers) {
    const temp = []

    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            if (!temp.includes(numbers[i] + numbers[j])) {
                temp.push(numbers[i] + numbers[j])
            }
            temp.push(numbers[i] + numbers[j])
        }
    }

    const answer = [...new Set(temp)]

    return answer.sort((a, b) => a - b)
}
```
위와같이 풀리면 풀리지만 뭔가 .. 다 넣어두고 `new Set`을 사용하는게 아닌가 싶다.
조건문을 걸어서 존재한다면 넣지 않는 방식으로 풀어보자.
```typescript
function solution(numbers) {
    const result = []

    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            if (!result.includes(numbers[i] + numbers[j])) {
                result.push(numbers[i] + numbers[j])
            }
        }
    }

    return result.sort((a, b) => a - b);
}
```

## 2016
```markdown
문제 설명
2016년 1월 1일은 금요일입니다.
2016년 a월 b일은 무슨 요일일까요?
두 수 a ,b를 입력받아
2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다.

예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
입출력 예
a	b	result
5	24	"TUE"
```

```typescript
function solution(a: number, b: number): string {
    const days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
    const date = new Date(`2016-${a}-${b}`);
    console.log(date); // 2016-05-23T15:00:00.000Z
    return days[date.getDay()];
}

console.log(solution(5, 24));
```