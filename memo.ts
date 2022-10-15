// 에라토스테네스 체를 이용해 3000까지의 수 중 소수인 수를 판별
function makePrime () {
  const numArr = new Array(100).fill(true);
  for (let i = 2; i**2 <= 3000; i++) {
    if (!numArr[i]) continue;
    for (let j = i**2; j <= 3000; j+= i) {
      numArr[j] = false;
    }
  }

  return numArr;
}

function solution (n:number[]) {
  const numArr = makePrime();
  let count = 0;

  for (let i = 2; i <= n.length; i++) {
    if (numArr[i]) count++;
  }
  return count;
}

console.log(solution([1,2,3,4]));