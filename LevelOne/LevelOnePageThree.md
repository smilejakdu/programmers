# 프로그래머스 레벨 1 페이지 3

## 목차
1. [두개뽑아서더하기](#두개뽑아서더하기)
2. [2016](#2016)
3. [포켓몬찾기](#포켓몬찾기)
4. [모의고사](#모의고사)
5. [소수만들기](#소수만들기)
6. [실패율](#실패율)


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

## 포켓몬찾기
```markdown
당신은 폰켓몬을 잡기 위한 오랜 여행 끝에, 홍 박사님의 연구실에 도착했습니다. 홍 박사님은 당신에게 자신의 연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
홍 박사님 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분합니다. 따라서 같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다. 예를 들어 연구실에 총 4마리의 폰켓몬이 있고, 각 폰켓몬의 종류 번호가 [3번, 1번, 2번, 3번]이라면 이는 3번 폰켓몬 두 마리, 1번 폰켓몬 한 마리, 2번 폰켓몬 한 마리가 있음을 나타냅니다. 이때, 4마리의 폰켓몬 중 2마리를 고르는 방법은 다음과 같이 6가지가 있습니다.

첫 번째(3번), 두 번째(1번) 폰켓몬을 선택
첫 번째(3번), 세 번째(2번) 폰켓몬을 선택
첫 번째(3번), 네 번째(3번) 폰켓몬을 선택
두 번째(1번), 세 번째(2번) 폰켓몬을 선택
두 번째(1번), 네 번째(3번) 폰켓몬을 선택
세 번째(2번), 네 번째(3번) 폰켓몬을 선택
이때, 첫 번째(3번) 폰켓몬과 네 번째(3번) 폰켓몬을 선택하는 방법은 한 종류(3번 폰켓몬 두 마리)의 폰켓몬만 가질 수 있지만, 다른 방법들은 모두 두 종류의 폰켓몬을 가질 수 있습니다. 따라서 위 예시에서 가질 수 있는 폰켓몬 종류 수의 최댓값은 2가 됩니다.
당신은 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에, 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 합니다. N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.
입출력 예
nums	        result
[3,1,2,3]	    2
[3,3,3,2,2,4]	3
[3,3,3,2,2,2]	2
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리, 2번 폰켓몬 한 마리, 4번 폰켓몬 한 마리를 고르면 되며, 따라서 3을 return 합니다.

입출력 예 #3
6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리와 2번 폰켓몬 두 마리를 고르거나, 혹은 3번 폰켓몬 두 마리와 2번 폰켓몬 한 마리를 고르면 됩니다. 따라서 최대 고를 수 있는 폰켓몬 종류의 수는 2입니다.
```

```typescript
function solution(nums:number[]): number {
    const set = new Set(nums);
    console.log(set); // Set(3) { 3, 1, 2 }
    const arr = Array.from(set);
    console.log(arr); // [3,1,2]

    return arr.length > nums.length/2 ? nums.length/2 : arr.length;
}

console.log(solution([3,1,2,3]));
```

## 모의고사
```markdown
문제 설명
수포자는 수학을 포기한 사람의 준말입니다.
수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

입출력                 예
answers	            return
[1,2,3,4,5]	        [1]
[1,3,2,4,2]	        [1,2,3]

입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2
모든 사람이 2문제씩을 맞췄습니다.
```

python 문제풀이
```python
def solution(answers):
    supo_list    = [[1, 2, 3, 4, 5],
                    [2, 1, 2, 3, 2, 4, 2, 5],
                    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    answer_list  = [0 , 0 , 0]

    for index in range(0 , len(answers)):
        if supo_list[0][index % len(supo_list[0])] == answers[index]:
            answer_list[0] += 1

        if supo_list[1][index % len(supo_list[1])] == answers[index]:
            answer_list[1] += 1

        if supo_list[2][index % len(supo_list[2])] == answers[index]:
            answer_list[2] += 1

    max_number  = max(answer_list)
    result_list = []

    for index in range(0 , len(answer_list)):
        if max_number == answer_list[index]:
            result_list.append(index + 1)

    return result_list
```

```typescript
function solution(nums:number[]) :number[] {
    let answer = [];
    let count = [0,0,0];
    
    let first  = [1,2,3,4,5];
    let second = [2,1,2,3,2,4,2,5];
    let third  = [3,3,1,1,2,2,4,4,5,5];

    for(let i = 0; i < nums.length; i++) {
        if(nums[i] === first[i % first.length]) count[0]++;
        if(nums[i] === second[i % second.length]) count[1]++;
        if(nums[i] === third[i % third.length]) count[2]++;
    }
    
    let max = Math.max(...count);
    for(let i = 0; i < count.length; i++) {
        if(count[i] === max) answer.push(i+1);
    }
    return answer;
}

console.log(solution([1,2,3,4,5])); // [1]
```

## 소수만들기

```typescript
function isPrime(num: number): boolean {
  if (num === 1) return false;
  for (let i = 2; i < num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function solution(nums: number[]): number {
  let result = 0;
  const dfs = (index: number, sum: number, count: number) => {
    if (count === 3) {
      if (isPrime(sum)) result++;
      return;
    }
    for (let i = index; i < nums.length; i++) {
      dfs(i + 1, sum + nums[i], count + 1);
    }
  };
  dfs(0, 0, 0);
  return result;
}

console.log(solution([1,2,7,6,4])); // 1
```

## 실패율

```typescript


```