# 프로그래머스 레벨 1 페이지 2

## 목차
1. [가운데글자가져오기](#가운데글자가져오기)
2. [수박수박수박수박수박수](#수박수박수박수박수박수)
3. [내적](#내적)
4. [문자열내림차순으로배치](#문자열내림차순으로배치)
5. [문자열다루기기본](#문자열다루기기본)
6. [약수의개수와덧셈](#약수의개수와덧셈)
7. [행렬의덧셈](#행렬의덧셈)
8. [부족한금계산하기](#부족한금계산하기)
9. [직사각형별찍기](#직사각형별찍기)


## 가운데글자가져오기
```typescript
/*
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	return
"abcde"	"c"
"qwer"	"we"
*/
function solution(s: string): string {
  const stringLength = s.length;
  const mid = Math.floor(stringLength / 2);
  // Math.floor 를 하게되면 소수점이하를 버리게 된다.
  return stringLength % 2 === 0 ? s[mid - 1] + s[mid] : s[mid];
}

console.log(solution('abcde'));
```

## 수박수박수박수박수박수
```typescript
/*
문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
n	return
3	"수박수"
4	"수박수박"
*/

function solution(n: number): string {
    let answer = '';
    for (let i = 0; i < n; i++) {
        if (i % 2 === 0) {
            answer += '수';
        } else {
            answer += '박';
        }
    }
    return answer;
}

console.log(solution(3));
```

## 내적
```typescript
/*
문제 설명
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

제한사항
a, b의 길이는 1 이상 1,000 이하입니다.
a, b의 모든 수는 -1,000 이상 1,000 이하입니다.
입출력 예
a	b	result
[1,2,3,4]	[-3,-1,0,2]	3
[-1,0,1]	[1,0,-1]	-2
*/

function solution(a: number[], b: number[]): number {
  return a.reduce((acc, cur, idx) => acc + cur * b[idx], 0);
}

console.log(solution([1, 2, 3, 4], [-3, -1, 0, 2]));
```

## 문자열내림차순으로배치
```typescript
/*
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

제한 사항
str은 길이 1 이상인 문자열입니다.
입출력 예
s	return
"Zbcdefg"	"gfedcbZ"
*/

function solution(s: string): string {
  return s
    .split("")
    .sort((a, b) => (a > b ? -1 : 1))
    .join("");
}

console.log(solution("Zbcdefg"));
```

## 문자열다루기기본
```typescript
/*
문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.
입출력 예
s	return
"a234"	false
"1234"	true
*/

function solution(s: string): boolean {
  // isNaN() 함수는 문자열이 숫자로 변환될 수 없을 때 true를 반환합니다.
  return s.length === 4 || s.length === 6 ? !isNaN(Number(s)) : false;
}

console.log(solution("a234"));
```

## 약수의개수와덧셈
```typescript
/*
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
입출력 예
left	right	result
13	  17	  43
24	  2e	  52
*/

function solution(left:number, right:number): number {
  let answer = 0;

  for (let i = left; i <= right; i++) {
    let count = 0;

    for (let j = 1; j <= i; j++) {
      // 약수의 개수를 구한다.
      if (i % j === 0) {
        count++;
      }
    }

    if (count % 2 === 0) {
      // 약수의 개수가 짝수면 더한다.
      answer += i;
    } else {
      // 약수의 개수가 홀수면 뺀다.
      answer -= i;
    }

  }
  return answer;
}

console.log(solution(13, 17));
```

## 행렬의덧셈
```typescript
function solution(arr1: [number[],number[]], arr2:[number[],number[]]) {
  return arr1.map((arrElement,i)=>{
    return arrElement.map((arrElementOfElement,j)=>{
      return arrElementOfElement+arr2[i][j]
    })
  })
}

console.log(solution([[1,2],[2,3]], [[3,4],[5,6]]));
console.log(solution([[1],[2]], [[3],[4]]));

function sumMatrix(A,B){
    return A.map((a,i) => a.map((b, j) => b + B[i][j]));
}

console.log(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]])) 
```

## 부족한금액계산하기
```typescript
/*
문제 설명
새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.

제한사항
놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수
입출력 예
price	money	count	result
3	    20	  4	    10
*/

// 제네릭 function 을 만들어준다.

function solution(price: number, money: number, count: number) :number {
  let result = 0;
  for (let i = 1; i <= count; i++){
    result += price * i;
  }
  return result > money ? result - money : 0
}

console.log(solution(3, 20, 4));
```

## 직사각형별찍기
```typescript
/*
문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

제한 조건
n과 m은 각각 1000 이하인 자연수입니다.
예시
입력

5 3
출력

*****
*****
*****
*/

// 제네릭 function 을 만들어준다.

function solution(n: number, m: number): string {
  let result = "";
  for (let i = 0; i < m; i++) {
    result += "*".repeat(n) + "\n";
  }
  return result;
}

console.log(solution(5, 3));
```