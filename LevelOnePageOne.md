# Programmers Level One Page One

## 목차
1. [평균구하기](#평균구하기)
2. [x만큼간격이있는n개의숫자](#x만큼간격이있는n개의숫자)
3. [나누어떨어지는숫자배열](#나누어떨어지는숫자배열)
4. [나머지1이되는수찾기](#나머지1이되는수찾기)
5. [내림차순으로배치](#내림차순으로배치)
6. [두정수사이의합](#두정수사이의합)
7. [문자열내p와y의개수](#문자열내p와y의개수)
8. [문자열을정수로바꾸기](#문자열을정수로바꾸기)
9. [서울에서김서방찾기](#서울에서김서방찾기)
10. [약수의합](#약수의합)
11. [음양더하기](#음양더하기)
12. [자릿수더하기](#자릿수더하기)
13. [자연수뒤집어배열로만들기](#자연수뒤집어배열로만들기)
14. [정수제곱근판별](#정수제곱근판별)
15. [제일작은수제거하기](#제일작은수제거하기)
16. [짝수와홀수구하기](#짝수와홀수구하기)
17. [하샤드수](#하샤드수)
18. [핸드폰번호가리기](#핸드폰번호가리기)
19. [없는숫자더하기](#없는숫자더하기)
20. [비밀지도](#비밀지도)


## 평균구하기

```typescript
/*
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
입출력 예

arr       return
[1,2,3,4]	2.5
[5,5]       5
 */

function solution(arr:number[]): number {
  const sum = arr.reduce((acc: number, cur: number) => acc + cur);
  return sum / arr.length;
}

// return array.reduce((a, b) => a + b) / array.length;
// 굳이 currentIndex 를 0 으로 하지 않아도 된다 default 값으로 0 으로 되니깐 0 으로 초기화 할 필요가 없다.

console.log(solution([1, 2, 3, 4])); // 2.5
```

## x만큼간격이있는n개의숫자
```typescript
/*
문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아,
x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.

입출력 예
x	  n	  answer
2	  5	  [2,4,6,8,10]
4	  3	  [4,8,12]
-4	2	  [-4, -8]
*/

function solution(x: number, n: number): number[] {
  let answer = [];
  let num = 0;
  for (let i = 0; i <n; i++) {
    num += x;
    answer.push(num);
  }
  return answer;
}

console.log(solution(2, 5)); // [2,4,6,8,10]
console.log(solution(4, 3)); // [4,8,12]
console.log(solution(-4, 2)); // [-4, -8]

// 다른사람의 풀이
// function solution(x, n) {
//   return Array(n).fill(x).map((v, i) => (i + 1) * v)
// }

// 미리 n개의 길이만큼의 배열을 만들고 x 로 값을 채워넣느다.
// 그리고 map 을 통해 각각의 값을 x 로 곱해준다.
```

## 나누어떨어지는숫자배열
```typescript
/*
문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.

입출력 예
arr	          divisor	    return
[5, 9, 7, 10]	5	          [5, 10]
[2, 36, 1, 3]	1	          [1, 2, 3, 36]
[3,2,6]	      10	        [-1]
*/
function solution(arr: number[], divisor: number): number[] {
  const result = arr.filter((number) => number % divisor ===0).sort((a,b)=>a-b);
  if (result.length === 0) return [-1];
  return result;
}

const arr = [5,9,7,10];
const divisor = 5;
console.log(solution(arr, divisor));
```

## 나머지1이되는수찾기
```typescript
/*
문제 설명
자연수 n이 매개변수로 주어집니다.
n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
답이 항상 존재함은 증명될 수 있습니다.

제한사항
3 ≤ n ≤ 1,000,000
입출력 예
n	result
10	3
12	11

입출력 예 #1

10을 3으로 나눈 나머지가 1이고, 3보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 3을 return 해야 합니다.
입출력 예 #2

12를 11로 나눈 나머지가 1이고, 11보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 11을 return 해야 합니다.
*/

function solution(n: number): number {
  for (let i = 1; i < n; i++) {
      if (n % i === 1) {
        return i;
      }
  }
}
console.log(solution(10)); // 3
```

## 내림차순으로배치
```typescript
/*
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다.
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
입출력 예
n	      return
118372	873211
*/

function solution(n: number): number {
  const sortedNumber = n
    .toString()
    .split('')
    .sort((a, b) => Number(b) - Number(a))
    .join('')
  return Number(sortedNumber);
}

console.log(solution(118372)); // 873211

// 다른 문제풀이를 보니깐
// return +sortedNumber; 이렇게도 가능하다고 한다.
```
## 두정수사이의합
```typescript
/*
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한 조건
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.
입출력 예

a	b	return
3	5	12
3	3	3
5	3	12
*/

function solutionOne(a: number,b : number): number {
  let bigger;
  let smaller;
  let result=0;
  if(a >= b){
    bigger = a;
    smaller = b;
    for(let i = b; i<=a; i++) {
      result +=i;
    }
  } else {
    bigger = b;
    smaller = a;
    for(let i = a; i <=b; i++){
      result +=i;
    }
  }
  return result;
}

const a = 3;
const b = 5
console.log(solutionOne(a,b));

// 위와 같이 풀수 있다. 하지만 만약에 Math.min 과 Math.max를 사용하게 되면 ??

function solutionTwo(a: number, b: number): number {
  let answer = 0;
  let min = Math.min(a, b);
  let max = Math.max(a, b);
  for (let i = min; i <= max; i++) {
    answer += i;
  }
  return answer;
}

console.log(solutionTwo(3, 5)); // 12
```

## 문자열내p와y의개수
```typescript
/*
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True,
다르면 False를 return 하는 solution를 완성하세요.
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
입출력 예
s	        answer
"pPoooyY"	true
"Pyy"	    false

*/

function solution(s: string) :boolean{
  let pCount = 0;
  let yCount = 0;

  s.split('').map(string => {
    if (string.toLowerCase() === 'p') pCount ++;
    else if (string.toLowerCase() === 'y') yCount ++;
  });
  return pCount === yCount
}

console.log(solution("pPoooyY")); // true

// 코드를 좀 더 깔끔하게 할 수 있을것 같다.

// 다른 사람의 풀이
function numPY(s: string): boolean {
  return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
}

// 생각을 조금 더 다르게 하셨다.
// 단순히 p 와 y 의 개수를 비교하는게 아니라 p 와 y 를 기준으로 문자열을 나누고 그 길이를 비교하는 방법이다.
// 그길이가 같으면 p 와 y 의 개수가 같다는 뜻이다.
```

## 문자열을정수로바꾸기
```typescript
/*
문자열을 정수로 바꾸기
문제 설명
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 "0"으로 시작하지 않습니다.

입출력 예
예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.
*/

function solution(s: string): number {
  return Number(s);
}

console.log(solution("1234")); // 1234
```

## 서울에서김서방찾기
```typescript
/*
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아,
"김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
"Kim"은 반드시 seoul 안에 포함되어 있습니다.

입출력 예
seoul	return
["Jane", "Kim"]	"김서방은 1에 있다"
*/

function solution(seoul: string[]): string {
  const kimIndex = seoul.indexOf('Kim');
  return `김서방은 ${kimIndex}에 있다`;
}

console.log(solution(["Jane", "Kim"])); // 김서방은 1에 있다
```

## 약수의합
```typescript
/*
약수의 합
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.

입출력 예
n	   return
12	28
5	  6

입출력 예 설명
입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
 */

function solution(n: number) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    if (n % i === 0) sum+= i;
  }
  return sum;
}

console.log(solution(12)); // 28
```

## 음양더하기
```typescript
/*
문제 설명
어떤 정수들이 있습니다.
이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

제한사항
absolutes의 길이는 1 이상 1,000 이하입니다.
absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
signs의 길이는 absolutes의 길이와 같습니다.
signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

입출력 예
absolutes	signs	              result
[4,7,12]	[true,false,true]	  9
[1,2,3]	  [false,false,true]	0
입출력 예 설명
입출력 예 #1

signs가 [true,false,true] 이므로, 실제 수들의 값은 각각 4, -7, 12입니다.
따라서 세 수의 합인 9를 return 해야 합니다.
입출력 예 #2

signs가 [false,false,true] 이므로, 실제 수들의 값은 각각 -1, -2, 3입니다.
따라서 세 수의 합인 0을 return 해야 합니다.
*/

function solution(absolutes: number[], signs: boolean[]): number {
  return absolutes.reduce((acc, cur, idx) => {
    return acc + (signs[idx] ? cur : -cur);
  }, 0);
}

console.log(solution([4, 7, 12], [true, false, true])); // 9
```

## 자릿수더하기
```typescript
/*
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수
입출력 예
N	  answer
123	6
987	24
*/

function solution(n: number) {
  return n
    .toString()
    .split("")
    .reduce((acc: number, cur) => acc + parseInt(cur),0);
}

/*
  return n
    .toString()
    .split("")
    .reduce((acc: number, cur: string) => acc + parseInt(cur));
   이렇게 하면 되지 않는데 ,
   default 값이 0 이 되지만 cur 의 타입이 string 이기 때문에
   에러가 발생한다. 그렇기때문에 0 을 넣어줘야한다.
 */

console.log(solution(123)); // 6
```

## 자연수뒤집어배열로만들기
```typescript
/*
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.

입출력 예
n	    return
12345	[5,4,3,2,1]
*/

import {log} from "console";

function solution(n: number): number[] {
  return n
    .toString()
    .split('')
    .reverse()
    .map((v) => parseInt(v));
}

log(solution(12345)); // [5,4,3,2,1]
```

## 정수제곱근판별
```typescript
/*
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.

입출력 예
n     return
121   144
3     -1

입출력 예 설명
입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.
*/

function solution(n) {
  let x = Math.sqrt(n);
  if(x % 1 === 0 ) return (x+1) * (x+1)
  else return -1;
}

console.log(solution(121)); // 144
// 121 -> 11 -> 12 -> 144

// 내장함수에서 Math.sqrt 를 사용하게 되면 제곱근을 구할 수 있다.
```

## 제일작은수제거하기
```typescript
/*
문제 설명
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

제한 조건
arr은 길이 1 이상인 배열입니다.
인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
입출력 예
arr	      return
[4,3,2,1]	[4,3,2]
[10]	    [-1]
*/

function solution(arr: number[]): number[] {
  // 리스트를 destructuring 하고 가장 최소의 수를 구한다.
  const min = Math.min(...arr);
  // 최소수의 index를 구한다.
  const index = arr.indexOf(min);
  arr.splice(index, 1);
  return arr.length ? arr : [-1];
}

console.log(solution([4, 3, 2, 1]));
```

## 짝수와홀수구하기
```typescript
/*
짝수와 홀수
문제 설명
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.

입출력 예
num	    return
3	      "Odd"
4	      "Even"
*/

function solutionOddAndEven(num:number):string {
  return num % 2 === 0 ? "Even" : "Odd";
}

console.log(solutionOddAndEven(3)); // Odd
```

## 하샤드수
```typescript
/*
문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
입출력 예
arr	return
10	true
12	true
11	false
13	false

입출력 예 설명
입출력 예 #1
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

입출력 예 #2
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

입출력 예 #3
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

입출력 예 #4
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.
*/

function solution(x: number): boolean {
  const sum = x
    .toString()
    .split('')
    .reduce((a, b) => a + parseInt(b),0);
  return x % sum === 0;
}

console.log(solution(10)); // true
```

## 핸드폰번호가리기
```typescript
/*
문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때,
전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
phone_number는 길이 4 이상, 20이하인 문자열입니다.

입출력 예
phone_number	return
"01033334444"	"*******4444"
"027778888"	"*****8888"
*/

function solution(phone_number: string): string {
  if (phone_number.length < 4 || phone_number.length > 20) {
    throw new Error('phone_number는 길이 4 이상, 20이하인 문자열입니다.');
  }
  // 뒤에서 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴
  const lastFour = phone_number.slice(-4);
  const asterisk = '*'.repeat(phone_number.length - 4);
  // phone_number 에서 -4 길이만큼 * 를 반복한다.
  return asterisk + lastFour;
}

console.log(solution("01033334444")); // *******4444
console.log(solution("027778888")); // *****8888
// 위에처럼 풀수도 있지만
// 졍규식을 사용하게되면 밑에 usedSolution 처럼 조금 더 간단하게 풀 수가 있다.

function usedRegularSolution(phone_number: string): string {
  return phone_number.replace(/\d(?=\d{4})/g, "*");
}
```

## 없는숫자더하기
```typescript
/*
없는 숫자 더하기
문제 설명
0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 원소 ≤ 9
numbers의 모든 원소는 서로 다릅니다.
입출력 예
numbers	result
[1,2,3,4,6,7,8,0]	14
[5,8,4,0,6,7,9]	6
*/

function solution(numbers: number[]): number {
  const sum = numbers.reduce((acc, cur) => acc + cur, 0);
  return 45 - sum;
}
```

## 비밀지도
```typescript
/*
네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다.
그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다.
다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다.
각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
"지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.

입력 형식
입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.

1 ≦ n ≦ 16
arr1, arr2는 길이 n인 정수 배열로 주어진다.
정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2n - 1을 만족한다.
출력 형식
원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.

입출력 예제
매개변수	값
n	      5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]
매개변수	값
n	      6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]
*/

function convertToBinary(dec,n) {
    let binary = dec.toString(2);
    if(binary.length < n) {
        binary = '0'.repeat(n-binary.length) + binary;
    }
    return binary;
}

function changeOneToSharp(binaryList) {
  let changeBinaryArrShop = [];

  binaryList.forEach((numString) => {
    // 이진수 string 을 리스트로바꿔서 반복문을 돌린다 만약에 1이 나오게되면 #으로 교체한다.
    let numList = numString.split("");
    numList.forEach((num, index) => {
      numList[index] = num === "1" ? "#" : " ";
    });
    changeBinaryArrShop.push(numList.join(""));
  });
  return changeBinaryArrShop;
}

function solution(n, arr1, arr2) {
  const binaryArr1 = arr1.map((num) => convertToBinary(num, n));
  const changedOneToSharpArr1 = changeOneToSharp(binaryArr1);
  const binaryArr2 = arr2.map((num) => convertToBinary(num, n));
  const changedOneToSharpArr2 = changeOneToSharp(binaryArr2);
// changedOneToSharpArr1 과 changedOneToSharpArr2 를 합쳐서 #이 하나라도 있으면 #으로 바꿔준다.
  const answer = changedOneToSharpArr1.map((num, index) => {
    let numList = num.split("");
    let numList2 = changedOneToSharpArr2[index].split("");
    numList.forEach((num, index) => {
      if (numList2[index] === "#") {
        numList[index] = "#";
      }
    });
    return numList.join("");
  });
  return answer;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]));
```