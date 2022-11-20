# Programmers Level Two Page One

## 목차
1. [최댓값과최소값](#최댓값과최소값)
2. [JadenCase문자열만들기](#JadenCase문자열만들기)
3. [올바른괄호](#올바른괄호)
4. [최솟값만들기](#최솟값만들기)
5. [다음큰수](#다음큰수)
6. [이진변환반복하기](#이진변환반복하기)
7. [카펫](#카펫)
8. [짝지어제거하기](#짝지어제거하기)
9. [영어끝말잇기](#영어끝말잇기)
10. [구명보트](#구명보트)
11. [N개의최소공배수](#N개의최소공배수)
12. [예상대진표](#예상대진표)
13. [점프와순간이동](#점프와순간이동)
14. [멀리뛰기](#멀리뛰기)
15. [캐시](#캐시)
16. [H-Index](#H-Index)
17. [괄호회전하기](#괄호회전하기)
18. [튜플](#튜플)

## 최댓값과최소값
```markdown
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
입출력 예
s	return
"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"
```
```ts
function solution(s: string) {
  const string_list = s.split(' ').map((item) =>{
    return parseInt(item);
  })

  const minStringNum = Math.min(...string_list);
  const maxStringNum = Math.max(...string_list);
  return `${minStringNum} ${maxStringNum}`;
}

console.log(solution("1 2 3 4"))
```

이렇게 풀었는데 다른사람들이 더 잘풀었다.

```typescript
function solution(s) {
    const arr = s.split(' ');

    return Math.min(...arr)+' '+Math.max(...arr);
}
console.log(solution("1 2 3 4"))
```

## JadenCase문자열만들기

```markdown
JadenCase란 모든 단어의 첫 문자가 대문자이고,
그 외의 알파벳은 소문자인 문자열입니다.
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
숫자는 단어의 첫 문자로만 나옵니다.
숫자로만 이루어진 단어는 없습니다.
공백문자가 연속해서 나올 수 있습니다.

입출력                         예
s	                        return
"3people unFollowed me"	    "3people Unfollowed Me"
"for the last week"	        "For The Last Week"
```

```ts
function solution(s: string): string {
  return s.split(' ').map((word) => {
    const first = word[0].toUpperCase()
    const rest = word.slice(1).toLowerCase()
    return first + rest
  }).join(' ')
}

console.log(solution("3people unFollowed me"));
```

이상태로 돌리게되면 에러가 발생하게 된다.
https://thisthat.dev/string-char-at-vs-string-bracket-notation/
이유는 위와같은 이유로 다음과 같이 다시 돌려야한다.

```ts
function solution(s) {
  return s.split(" ").map(v => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase()).join(" ");
}
console.log(solution("3people unFollowed me"));
```

## 올바른괄호
```markdown
올바른 괄호
문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
입출력 예
s	            answer
"()()"	        true
"(())()"	    true
")()("	        false
"(()("	        false
```

```ts
function solution(s: string){
  const string = s.split('');
  let count = 0;
  for(let i = 0; i < string.length; i++) {
    string[i] === '(' ? count++ : count--;
    if(count < 0) return false;
  }
  return count === 0;
}

console.log(solution("()()"));
console.log(solution("(())()"));
console.log(solution(")()("));
```

## 최솟값만들기

```markdown
문제 설명
길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면

A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
즉, 이 경우가 최소가 되므로 29를 return 합니다.

배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

제한사항
배열 A, B의 크기 : 1,000 이하의 자연수
배열 A, B의 원소의 크기 : 1,000 이하의 자연수
입출력 예
A	            B	        answer
[1, 4, 2]	    [5, 4, 4]	29
[1,2]	        [3,4]	    10
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
A에서 첫번째 숫자인 1, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 4) 다음, A에서 두번째 숫자인 2, B에서 첫번째 숫자인 3을 뽑아 곱하여 더합니다. (누적된 값 : 4 + 6 = 10)
이 경우가 최소이므로 10을 return 합니다.
```

```ts
function solution(A:number[], B:number[]) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  return A.reduce((acc, cur, idx) => acc + cur * B[idx], 0);
}

console.log(solution([1, 4, 2], [5, 4, 4])); // 29
```

## 다음큰수
```markdown
다음 큰 숫자
문제 설명
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

제한 사항
n은 1,000,000 이하의 자연수 입니다.
입출력 예
n	result
78	83
15	23
입출력 예 설명
입출력 예#1
문제 예시와 같습니다.
입출력 예#2
15(1111)의 다음 큰 숫자는 23(10111)입니다.

생각법----------------------------
1. 숫자를 받고 2진수로 변환한다. -> toString(2)
2. 1의 갯수를 센다. -> filter((num) => num === '1').length
3. 1의 갯수가 같은 숫자를 찾는다. -> 2 번의 조건에서 같은 값을 하났기 찾는다.
4. 1의 갯수가 같은 숫자중 가장 작은 숫자를 찾는다. 하나씩 찾는거니 찾을때 바로 return 하면 된다.
```
```ts

function solution(n:number) {
  const nCount = n.toString(2).split('').filter(v => v === '1').length;
  while (true) {
    n++;
    if (nCount === n.toString(2).split('').filter(v => v === '1').length) {
      return n;
    }
  }
}
```

## 이진변환반복하기

```markdown
Finn은 요즘 수학공부에 빠져 있습니다.
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6         = 15
7 + 8             = 15
15                = 15

자연수 n이 매개변수로 주어질 때,
연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.

입출력 예
n	  result
15	4

입출력 예 설명
입출력 예#1
문제의 예시와 같습니다.
```

```ts
function solution(n:number) {
    let result = 0;
    for(let i=1; i<=n; i++) {
        let sum = 0;
        for(let j=i; j<=n; j++){
            sum += j;
            if(sum === n){
                result++;
                break;
            }
            if(sum > n) {
                break;
            }
        }
    }
    return result;
}

console.log(solution(15)); // 4
```

## 짝지어제거하기
```markdown
짝지어 제거하기
문제 설명
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.
예를 들어, 문자열 S = baabaa 라면
b aa baa → bb aa → aa →
의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

제한사항
문자열의 길이 : 1,000,000이하의 자연수
문자열은 모두 소문자로 이루어져 있습니다.

입출력 예
s	      result
baabaa	1
cdcd	  0

입출력 예 설명
입출력 예 #1
위의 예시와 같습니다.
입출력 예 #2
문자열이 남아있지만 짝지어 제거할 수 있는 문자열이 더 이상 존재하지 않기 때문에 0을 반환합니다.

풀이생각 -------------
1. 문자열을 배열로 만들어서
2. 배열의 길이가 0이 될때까지 반복
3. 배열의 첫번째 요소와 두번째 요소가 같으면
```

```ts
function solution(s:string) {
    let stack = [];
    for(let i=0; i<s.length; i++) {
        if(stack[stack.length-1] === s[i]) {
            stack.pop();
        } else {
            stack.push(s[i]);
        }
    }
    return stack.length === 0 ? 1 : 0;
}
```

위와 같이 풀면 시간초과로 풀리지 않는다.

```ts
function solution(s) {
    let stack = [];

    s.split("").forEach(ch => {
        if (stack[stack.length-1] === ch) {
            stack.pop();
        }
        else {
            stack.push(ch);
        }
    });
    return stack.length == 0 ? 1 : 0;
}
```

이렇게 풀면 통과하게 된다.
흠... index 를 가져와서 리스트에서 index 로 찾는것보다 .
바로 `ch` 를 받아서 `stack[stack.length-1] === ch` 비교해서 그런것 같다.

## 영어끝말잇기

```markdown
1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
이전에 등장했던 단어는 사용할 수 없습니다.
한 글자인 단어는 인정되지 않습니다.
다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.

tank → kick → know → wheel → land → dream → mother → robot → tank

위 끝말잇기는 다음과 같이 진행됩니다.

1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
(계속 진행)
끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.

사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

제한 사항
끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수입니다.
words는 끝말잇기에 사용한 단어들이 순서대로 들어있는 배열이며, 길이는 n 이상 100 이하입니다.
단어의 길이는 2 이상 50 이하입니다.
모든 단어는 알파벳 소문자로만 이루어져 있습니다.
끝말잇기에 사용되는 단어의 뜻(의미)은 신경 쓰지 않으셔도 됩니다.
정답은 [ 번호, 차례 ] 형태로 return 해주세요.
만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.
입출력 예
n	words	result
3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]
입출력 예 설명
입출력 예 #1
3명의 사람이 끝말잇기에 참여하고 있습니다.

1번 사람 : tank, wheel, mother
2번 사람 : kick, land, robot
3번 사람 : know, dream, tank
와 같은 순서로 말을 하게 되며, 3번 사람이 자신의 세 번째 차례에 말한 tank라는 단어가 1번 사람이 자신의 첫 번째 차례에 말한 tank와 같으므로 3번 사람이 자신의 세 번째 차례로 말을 할 때 처음 탈락자가 나오게 됩니다.

입출력 예 #2
5명의 사람이 끝말잇기에 참여하고 있습니다.

1번 사람 : hello, recognize, gather
2번 사람 : observe, encourage, refer
3번 사람 : effect, ensure, reference
4번 사람 : take, establish, estimate
5번 사람 : either, hang, executive
와 같은 순서로 말을 하게 되며,
이 경우는 주어진 단어로만으로는 탈락자가 발생하지 않습니다.
따라서 [0, 0]을 return하면 됩니다.
```

```ts
function solution(n:number, words:string[]):number[] {
  let idx;
  const usedWords: string[] = [];
  for (let i = 0; i < words.length; i++) {
    // 끝말잇기 틀린 경우
    if (i > 0 && (words[i - 1][words[i - 1].length - 1] !== words[i][0])) {
      idx = i;
      return [idx % n + 1, Math.floor(idx / n) + 1];
    }
    // 이미 사용한 단어인 경우
    if (usedWords.includes(words[i])) {
      idx = i + 1;
      return [idx % n === 0 ? n : idx % n, Math.ceil(idx / n)];
    }
    usedWords.push(words[i]);
  }
  return [0, 0];
}
```

## 구명보트
```markdown

```

```ts
function solution(people: number[], limit: number): number {
  const sortedPeople = people.sort((a, b) => a - b);
  let sumWeight = 0;
  let result = 0;
  sortedPeople.map((weight) => {
    if (sumWeight + weight <= limit) {
      sumWeight += weight;
    } else {
      sumWeight = weight;
      result++;
    }
  });
  return result + 1;
}

console.log(solution([70, 50, 80, 50], 100)); // 3
console.log(solution([70, 80, 50], 100)); // 3
```
이렇게 풀어서 제출하게 되면 , 기본은 통과하게 되나 정답을 돌리게되면
통과하지 못한다. 다른 사람들의 코드를 봤는데..그닥 이해를 하지못했다. ㅠㅠㅠ
다음에 다시 풀어봐야겠다.

## N개의최소공배수
```markdown
N개의 최소공배수
문제 설명
두 수의 최소공배수(Least Common Multiple)란 입력된
두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
예를 들어 2와 7의 최소공배수는 14가 됩니다.
정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.
입출력 예
arr	        result
[2,6,8,14]	168
[1,2,3]	    6
```

```ts
function nlcm(num) {
 return num.reduce((a,b) => a*b / gcd(a,b))  
}

function gcd(a, b) {
  return a % b ? gcd(b, a%b) : b
}

console.log(nlcm([2,6,8,14]));
console.log(nlcm([1,2,3,5,7,11,13])) //30030
```

위와같이 간단히 푸신분이 계셨다. 깔끔하게 잘 푸셨다.

## 예상대진표

```markdown
예상 대진표
문제 설명
△△ 게임대회가 개최되었습니다.
이 대회는 N명이 참가하고, 토너먼트 형식으로 진행됩니다.
N명의 참가자는 각각 1부터 N번을 차례대로 배정받습니다.
그리고, 1번↔2번, 3번↔4번, ... , N-1번↔N번의 참가자끼리 게임을 진행합니다.
각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다.
이때, 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다.
만약 1번↔2번 끼리 겨루는 게임에서 2번이 승리했다면 다음 라운드에서 1번을 부여받고, 3번↔4번에서 겨루는 게임에서 3번이 승리했다면 다음 라운드에서 2번을 부여받게 됩니다.
게임은 최종 한 명이 남을 때까지 진행됩니다.

이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 궁금해졌습니다.
게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,
처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요.
단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.

제한사항
N : 21 이상 220 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)
A, B : N 이하인 자연수 (단, A ≠ B 입니다.)
입출력 예
N	A	B	answer
8	4	7	3
입출력 예 설명
입출력 예 #1
첫 번째 라운드에서 4번 참가자는 3번 참가자와 붙게 되고, 7번 참가자는 8번 참가자와 붙게 됩니다. 항상 이긴다고 가정했으므로 4번 참가자는 다음 라운드에서 2번이 되고, 7번 참가자는 4번이 됩니다. 두 번째 라운드에서 2번은 1번과 붙게 되고, 4번은 3번과 붙게 됩니다. 항상 이긴다고 가정했으므로 2번은 다음 라운드에서 1번이 되고, 4번은 2번이 됩니다. 세 번째 라운드에서 1번과 2번으로 두 참가자가 붙게 되므로 3을 return 하면 됩니다.
```

```ts
function solution(n: number, a:number, b:number){
    let result = 0;
    while(a !== b){
        a = Math.ceil(a/2);
        b = Math.ceil(b/2);
        result++;
    }
    return result;
}


console.log(solution(8,4,7)); // 3
```

## 점프와순간이동

```markdown
문제 설명
OO 연구소는 한 번에 K 칸을 앞으로 점프하거나, (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동을 할 수 있는 특수한 기능을 가진 아이언 슈트를 개발하여 판매하고 있습니다.
이 아이언 슈트는 건전지로 작동되는데, 순간이동을 하면 건전지 사용량이 줄지 않지만, 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 듭니다.
그러므로 아이언 슈트를 착용하고 이동할 때는 순간 이동을 하는 것이 더 효율적입니다.
아이언 슈트 구매자는 아이언 슈트를 착용하고 거리가 N 만큼 떨어져 있는 장소로 가려고 합니다.
단, 건전지 사용량을 줄이기 위해 점프로 이동하는 것은 최소로 하려고 합니다.
아이언 슈트 구매자가 이동하려는 거리 N이 주어졌을 때, 사용해야 하는 건전지 사용량의 최솟값을 return하는 solution 함수를 만들어 주세요.

예를 들어 거리가 5만큼 떨어져 있는 장소로 가려고 합니다.
아이언 슈트를 입고 거리가 5만큼 떨어져 있는 장소로 갈 수 있는 경우의 수는 여러 가지입니다.

처음 위치 0 에서 5 칸을 앞으로 점프하면 바로 도착하지만, 건전지 사용량이 5 만큼 듭니다.
처음 위치 0 에서 2 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 2) x 2에 해당하는 위치로 이동할 수 있으므로 위치 4로 이동합니다.
이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 3 만큼 듭니다.
처음 위치 0 에서 1 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 1) x 2에 해당하는 위치로 이동할 수 있으므로 위치 2로 이동됩니다.
이때 다시 순간이동 하면 (현재까지 온 거리 : 2) x 2 만큼 이동할 수 있으므로 위치 4로 이동합니다. 이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 2 만큼 듭니다.
위의 3가지 경우 거리가 5만큼 떨어져 있는 장소로 가기 위해서 3번째 경우가 건전지 사용량이 가장 적으므로 답은 2가 됩니다.

제한 사항
숫자 N: 1 이상 10억 이하의 자연수
숫자 K: 1 이상의 자연수
입출력 예
N	result
5	2
6	2
5000	5
입출력 예 설명
입출력 예 #1
위의 예시와 같습니다.

입출력 예 #2
처음 위치 0 에서 1 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 1) x 2에 해당하는 위치로 이동할 수 있으므로 위치 2로 이동합니다.
이때 1 칸을 앞으로 점프하면 위치3으로 이동합니다. 이때 다시 순간이동 하면 (현재까지 온 거리 : 3) x 2 이동할 수 있으므로 위치 6에 도착합니다. 이 경우가 건전지 사용량이 가장 적으므로 2를 반환해주면 됩니다.
```

```ts
function solution(n: number) {
    let result = 0;
    while (n > 0) {
        if (n % 2 === 0) {
            n /= 2; // 순간이동
        } else {
            n -= 1; // 점프
            result++; // 점프하면 에러지를 하나 소비하게 된다.
        }
    }
    return result;
}

console.log(solution(5)); // 2
```

## 멀리뛰기

```markdown
효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)
의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다.
멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 
여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요.
예를 들어 4가 입력된다면, 5를 return하면 됩니다.
```
`1234567` 은 왜 나누는걸까 ?;;;
```ts
function solution(n:number) :number {
    let result = 0;
    let dp = [1, 2];
    for (let i = 2; i < n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
    }
    result = dp[n - 1];
    return result;
}

console.log(solution(4));
```

## 캐시 

```markdown
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데,
제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 
제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

입출력 예제
캐시크기(cacheSize)	도시이름(cities)	실행시간
3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25
```

```ts
function solution(cacheSize:number, cities:string[]) :number {
    let result = 0;
    let cache = [];
    
    if (cacheSize === 0) {
        return cities.length * 5;
    }
    
    for (let i = 0; i < cities.length; i++) {
        let city = cities[i].toLowerCase();
        let index = cache.indexOf(city);
        
        if (index === -1) {
            result += 5;
            if (cache.length >= cacheSize) {
                cache.shift();
            }
        } else {
            result += 1;
            cache.splice(index, 1);
        }
        cache.push(city);
    }
    return result;
}

console.log(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]));
```

## H-Index

```markdown
H-Index
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중,
h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	      return
[3, 0, 6, 1, 5]	3
```

```ts
function solution(citations: number[]) {
  let result = 0;
  const sortedCitations = citations.sort((a, b) => b - a);
  // 내림차순으로 정렬한다.

  for (let i = 0; i < sortedCitations.length; i++) {
    if (sortedCitations[i] >= i + 1) {
      result = i + 1;
    }
  }

  return result;
}

console.log(solution([3, 0, 6, 1, 5])); // 3
```

## 괄호회전하기

```markdown
괄호 회전하기
문제 설명
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다.
예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다.
예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때
s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
s의 길이는 1 이상 1,000 이하입니다.
입출력 예
s	result
"[](){}"	3
"}]()[{"	2
"[)(]"	0
"}}}"	0
```
1. 문제를 풀었으나 통과하지 못해서 다시 풀고나서 올려볼까 합니다.


## 튜플

```markdown
튜플
문제 설명
셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다.
n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.

(a1, a2, a3, ..., an)
튜플은 다음과 같은 성질을 가지고 있습니다.

중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
튜플의 원소 개수는 유한합니다.
원소의 개수가 n개이고,
중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수),
이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.

{{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}
예를 들어 튜플이 (2, 1, 3, 4)인 경우 이는

{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
와 같이 표현할 수 있습니다. 이때, 집합은 원소의 순서가 바뀌어도 상관없으므로

{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
{{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}
는 모두 같은 튜플 (2, 1, 3, 4)를 나타냅니다.

특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때,
s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

[제한사항]
s의 길이는 5 이상 1,000,000 이하입니다.
s는 숫자와 '{', '}', ',' 로만 이루어져 있습니다.
숫자가 0으로 시작하는 경우는 없습니다.
s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.
s가 표현하는 튜플의 원소는 1 이상 100,000 이하인 자연수입니다.
return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어집니다.

[입출력 예]
s	                              result
"{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
"{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
"{{20,111},{111}}"	            [111, 20]
"{{123}}"	                      [123]
"{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]
```

```ts
function solution(s:string) {
  const result:number[] = [];
  const arr:number[][] = s.split('},{')
    .map((v) => v.replace(/{/g, '') // /{/g 를 하게되면 { 를 모두 찾아서 ''로 바꿔준다.
      .replace(/}/g, '')
      .split(',')
      .map((v) => parseInt(v)));

  arr.forEach(arr_list => {
    arr_list.forEach(value => {
      if (!result.includes(value)) result.push(value);
    });
  });
  return result;
}

console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"));
console.log(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"));
```

```ts
    arr.map((v) => {
        v.map((v) => {
            if (!result.includes(v)) {
                result.push(v);
            }
        });
    });
```
이렇게해도 풀린다 무슨차이가 있는걸까 ??
https://d-cron.tistory.com/11
https://dream-frontend.tistory.com/341

위의 두개의 링크를 보니 이해가 되었다.
나중에 좀더 자바스크립트 책을 봐야겠단 생각을 했다.
암튼 성능면에서 map 이 더 좋다고 하니 map으로 변경했다.


