list = [ 9, 22, 3, 7, 4, 5]
# O(n)
def max(list):
  # 0을 넣으면 음수일 때 계속 0만 나와서 배열에서 비교 X
  result = list[0] 

  # list[1:] 은 0번째에 자기자신과 비교하지 못하게 하려고   (시간 손실)
  for num in list[1:]: 
  
    if result < num : # max 구하기
      result = num  
  
  return result

def min(list):
  result = list[0]
  for i in range(1, len(list)):

    if result > list[i]:
      result = list[i]
  return result
# max
print('max =>',max(list))
print('min =>',min(list))