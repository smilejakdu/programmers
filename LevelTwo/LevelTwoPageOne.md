# Programmers Level One Page One

## 목차
1. [최댓값과최소값](#최댓값과최소값)
2. [JadenCase문자열만들기](#JadenCase문자열만들기)
3. [올바른괄호](#올바른괄호)

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