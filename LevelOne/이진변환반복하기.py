def solution(s):
    transformation_count = 0  # 이진 변환 횟수
    zero_count = 0  # 제거된 모든 0의 개수

    while s != "1":
        # 현재 문자열에서 0의 개수를 셉니다.
        count_zeros = s.count('0')
        zero_count += count_zeros

        # 문자열에서 0을 모두 제거합니다.
        s = s.replace("0", "")

        # 문자열의 길이를 2진법으로 변환합니다.
        length = len(s)
        s = bin(length)[2:]  # '0b' 접두사를 제외하고 순수한 이진수 문자열로 변환

        # 이진 변환 횟수를 증가시킵니다.
        transformation_count += 1

    return [transformation_count, zero_count]


# 테스트 예제
print(solution("110010101001"))  # 예상 출력: [3, 8]
print(solution("01110"))  # 예상 출력: [3, 3]
print(solution("1111111"))  # 예상 출력: [4, 1]
