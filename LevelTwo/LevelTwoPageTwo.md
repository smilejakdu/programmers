# Programmers Level Two Page Two

## 목차
1. [위장](#위장)
2. [n^2배열자르기](#n^2배열자르기)



## 위장

[위장](https://programmers.co.kr/learn/courses/30/lessons/42578) 문제를 풀어보자.
```markdown
위장
문제 설명
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.
입출력 예
clothes	return
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3

입출력 예 설명
예제 #1
headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.
1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses
   예제 #2
   face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

1. crow_mask
2. blue_sunglasses
3. smoky_makeup
```

```ts
function solution(clothes: string[][]): number {
  const map = new Map<string, number>();
  clothes.map((clothe) => {
    const [name, type] = clothe;
    map.set(type, (map.get(type) || 0) + 1); 
    // 만약 0 부터 해야했다면 그냥 map.get(type) || 0 만 해줘야한다.
    // 의상이 존재한다면 곧바로 +1 이 되기때문에 가능하다.
  });
  console.log([...map.values()]); // [2, 1]
  return [...map.values()].reduce((acc, cur) => {
    return acc * (cur + 1);
  }, 1) - 1; // 아무것도 안입는 경우를 제외
  // acc 는 이전까지의 결과값, cur은 현재값
  // 1 * (2 + 1) = 3
  // 3 * (1 + 1) = 6
}

console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]));
console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]));
```

## n^2배열자르기

```markdown
n^2 배열 자르기
문제 설명
정수 n, left, right가 주어집니다.
다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
정수 n, left, right가 매개변수로 주어집니다.
주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 107
0 ≤ left ≤ right < n2
right - left < 105

입출력 예
n	  left	right	result
3	  2	    5	    [3,2,2,3]
4	  7	    14	  [4,3,3,3,4,4,4,4]
```

```ts
function solution(n:number, left:number, right:number) {
  const result = [];
  let count = 0;
  
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (count >= left && count <= right) {
        result.push(Math.max(i, j));
      }
      count++;
    }
  }
  
  return result;
}

console.log(solution(3,2,5));
```