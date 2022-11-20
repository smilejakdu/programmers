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
10. [최대공약수와최소공배수](#최대공약수와최소공배수)
11. [이상한문자만들기](#이상한문자만들기)
12. [예산](#예산)
13. [비밀지도](#비밀지도)
14. [최소직사각형](#최소직사각형)
15. [문자열내마음대로정하기](#문자열내마음대로정하기)
16. [k번째수](#k번째수)
17. [숫자문자열과영단어](#숫자문자열과영단어)
18. [모음사전](#모음사전)


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

## 최대공약수와 최소공배수

```typescript
/*
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

  제한 사항
두 수는 1이상 1000000이하의 자연수입니다.
  입출력 예
n	m	return
3	12	[3, 12]
2	5	[1, 10]
*/
```

## 이상한문자만들기
```typescript
/*
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
입출력 예
s	return
"try hello world"	"TrY HeLlO WoRlD"
*/

function solution(s: string): string {
  return s
    .split(" ")
    .map((word) =>
      word
        .split("")
        .map((char, index) => (index % 2 === 0 ? char.toUpperCase() : char.toLowerCase()))
        .join("")
    )
    .join(" ");
}

console.log(solution("try hello world"));

// solution two
function solution(s: string) {
  let stringList: string[] = s.split(" ");
  let answer = "";
  stringList.map(function (element) {
    for (let i = 0; i < element.length; i++) {
      answer += (i + 1) % 2 == 0 ? element[i].toLowerCase() : element[i].toUpperCase();
    }
    answer += " ";
  });
  return answer.slice(0, -1);
}

```

## 예산

```typescript
/*
S사에서는 각 부서에 필요한 물품을 지원해 주기 위해 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다.
그러나, 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다. 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다.
예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.

부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

제한사항
d는 부서별로 신청한 금액이 들어있는 배열이며, 길이(전체 부서의 개수)는 1 이상 100 이하입니다.
d의 각 원소는 부서별로 신청한 금액을 나타내며, 부서별 신청 금액은 1 이상 100,000 이하의 자연수입니다.
budget은 예산을 나타내며, 1 이상 10,000,000 이하의 자연수입니다.
입출력 예
d	          budget	  result
[1,3,2,5,4]	9	        3
[2,2,3,3]	  10	      4
입출력 예 설명
입출력 예 #1
각 부서에서 [1원, 3원, 2원, 5원, 4원]만큼의 금액을 신청했습니다.
만약에, 1원, 2원, 4원을 신청한 부서의 물품을 구매해주면 예산 9원에서 7원이 소비되어 2원이 남습니다.
항상 정확히 신청한 금액만큼 지원해 줘야 하므로 남은 2원으로 나머지 부서를 지원해 주지 않습니다.
위 방법 외에 3개 부서를 지원해 줄 방법들은 다음과 같습니다.
1원, 2원, 3원을 신청한 부서의 물품을 구매해주려면 6원이 필요합니다.
1원, 2원, 5원을 신청한 부서의 물품을 구매해주려면 8원이 필요합니다.
1원, 3원, 4원을 신청한 부서의 물품을 구매해주려면 8원이 필요합니다.
1원, 3원, 5원을 신청한 부서의 물품을 구매해주려면 9원이 필요합니다.
3개 부서보다 더 많은 부서의 물품을 구매해 줄 수는 없으므로 최대 3개 부서의 물품을 구매해 줄 수 있습니다.

입출력 예 #2
모든 부서의 물품을 구매해주면 10원이 됩니다. 따라서 최대 4개 부서의 물품을 구매해 줄 수 있습니다.
*/

function solution(d: number[], budget: number): number {
    let answer = 0;
    d.sort((a,b)=>a-b);
    for(let i=0;i<d.length;i++){
        if(budget>=d[i]) {
            budget-=d[i];
            answer++;
        }
    }
    return answer;
}

console.log(solution([1,3,2,5,4],9));
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

function convertToBinary(dec:number){
    let binary = dec.toString(2);
    // 10진수를 2진수로 변환 앞에 자리가 0이면 안나오므로 0을 붙여준다.
    if(binary.length < 5){
        binary = "0" + binary;
    }
    return binary;
}

function changeOneToSharp(binaryList: string[]) {
  let changeBinaryArrShop: string[] = [];

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

function solution(n:number, arr1:number[], arr2:number[]) {
  const binaryArr1 = arr1.map((num) => convertToBinary(num));
  const changedOneToSharpArr1 = changeOneToSharp(binaryArr1);
  console.log(changedOneToSharpArr1)
  const binaryArr2 = arr2.map((num) => convertToBinary(num));
  const changedOneToSharpArr2 = changeOneToSharp(binaryArr2);
  console.log(changedOneToSharpArr2);
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
```
## 최소직사각형
```typescript
/*
문제 설명
명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다.
다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다.
이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

명함 번호	  가로 길이	  세로 길이
1	        60	      50
2	        30	      70
3	        60	      30
4	        80	      40

가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다.
하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다.
이때의 지갑 크기는 4000(=80 x 50)입니다.

모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes 가 매개변수로 주어집니다.
모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때,
지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

제한사항
sizes의 길이는 1 이상 10,000 이하입니다.
sizes의 원소는 [w, h] 형식입니다.
w는 명함의 가로 길이를 나타냅니다.
h는 명함의 세로 길이를 나타냅니다.
w와 h는 1 이상 1,000 이하인 자연수입니다.

입출력 예
sizes	                                          result
[[60, 50], [30, 70], [60, 30], [80, 40]]	      4000
[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	  120
[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	  133
*/

function solution(sizes: number[][]): number {
  const width = Math.max(...sizes.map((size) => Math.max(...size)));
  const height = Math.max(...sizes.map((size) => Math.min(...size)));
  return width * height;
}

console.log(solution([[60, 50], [30, 70], [60, 30], [80, 40]])); // 4000
// console.log(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])); // 120
// console.log(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])); // 133
```

## 문자열내마음대로정하기

```typescript
/*
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때,
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

제한 조건
strings는 길이 1 이상, 50이하인 배열입니다.
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
모든 strings의 원소의 길이는 n보다 큽니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

입출력 예
strings	                  n	        return
["sun", "bed", "car"]	    1	        ["car", "bed", "sun"]
["abce", "abcd", "cdx"]	  2	        ["abcd", "abce", "cdx"]

입출력 예 설명
입출력 예 1
"sun", "bed", "car"의 1번째 인덱스 값은 각각 "u", "e", "a" 입니다.
이를 기준으로 strings를 정렬하면 ["car", "bed", "sun"] 입니다.

입출력 예 2
"abce"와 "abcd", "cdx"의 2번째 인덱스 값은 "c", "c", "x"입니다.
따라서 정렬 후에는 "cdx"가 가장 뒤에 위치합니다.
"abce"와 "abcd"는 사전순으로 정렬하면 "abcd"가 우선하므로, 답은 ["abcd", "abce", "cdx"] 입니다.
*/

function solution(strings: string[], n: number):string[] {
  return strings.sort((a, b) => {
    if (a[n] === b[n]) {
      return a > b ? 1 : -1;
    }
    return a[n] > b[n] ? 1 : -1;
  });
}

console.log(solution(["sun", "bed", "car"], 1)); // ["car", "bed", "sun"]
```

## 숫자문자열과영단어

```markdown
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478    → "one4seveneight"
234567  → "23four5six7"
10203   → "1zerotwozero3"

이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine

제한사항
1 ≤ s의 길이 ≤ 50
s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

입출력 예
s	                result
"one4seveneight"	1478
"23four5six7"	    234567
"2three45sixseven"	234567
"123"	            123
```
`python` 문제 풀이  
```python
def solution(s):
    number_list = [
        'zero', 'one', 'two', 'three',
        'four', 'five', 'six', 'seven',
        'eight', 'nine'
    ]

    if s.isdigit():
        return int(s)

    for index, number in enumerate(number_list):
        s = s.replace(number, str(index))

    return int(s)
```

`typescript` 문제풀이
```typescript
function solution(s: string) {
  const numList = [
    'zero', 'one', 'two', 'three',
    'four', 'five', 'six', 'seven',
    'eight', 'nine'
  ];
  
  if (s.match(/^\d+$/)) {
    return parseInt(s, 10);
  }
  
  numList.map((num, index) => {
    s = s.replace(new RegExp(num, 'g'), index);
  });
  
  return parseInt(s, 10);
}

console.log(solution()); // 
```

## 모음사전 

```markdown
문제 설명
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

제한사항
word의 길이는 1 이상 5 이하입니다.
word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
입출력 예
word	result
"AAAAE"	6
"AAAE"	10
"I"	1563
"EIO"	1189
입출력 예 설명
입출력 예 #1

사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA", "AAA", "AAAA", "AAAAA", "AAAAE", ... 와 같습니다. "AAAAE"는 사전에서 6번째 단어입니다.

입출력 예 #2

"AAAE"는 "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU"의 다음인 10번째 단어입니다.

입출력 예 #3

"I"는 1563번째 단어입니다.

입출력 예 #4

"EIO"는 1189번째 단어입니다.
```

```ts
function solution(word: string): number {
    const alphabet = ["A", "E", "I", "O", "U"];
    const wordLength = word.length;
    let result = 0;

    for (let i = 0; i < wordLength; i++) {
        const index = alphabet.indexOf(word[i]);
        result += index * Math.pow(5, wordLength - i - 1) + 1;
    }

    return result;
}

console.log(solution("AAAAE")); // 6
```