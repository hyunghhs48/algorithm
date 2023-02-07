# 홀 / 짝 판별

# 짝수
def isEven(num):
  # 홀수인지 짝수인지 판단
  # 2로 나눠서 '나머지'가 0인지

  # 짝수면 true, 홀수면 false
  return num % 2 == 0

print(isEven(3))
print(isEven(4))