# print(123)
# print('차은우')
# print("차은우")
# print(123+456)
#
# fullname='슈퍼 에이전트 하이퍼 초필살 드래곤'
# print(fullname)
# print('차은우'[0])
#
# 중고차=['k5', 'white', 5000]
# 중고차[1]='black'
# print(중고차)
#
# 중고차2={
#     'brand':'bmw',
#     'model':'520d'
# }
# 중고차2['brand']=123
# print(중고차2['brand'])


# 재고량 = 10
#
# if 재고량>0 :
#     print('지금 주문 가능합니다')
# else:
#     print('품절되었습니다')

# 재고=['K5', 'BMW', 'Tico']
# if 'K5' in 재고:
#     print('주문 가능합니다.')

#반복문

# for i in range(1,7,2):
#     print(i)
#
# 중고차들=['BMW', 'Tico', 'K5']
# for i in 중고차들:
#     print(i)

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         a=numbers
#         count = 0
#
#         for j in range(i+1, len(a)):
#             if a[i]<a[j]:
#                 answer.append(a[j])
#                 break
#             else:
#                 count+=1
#                 print(a[j], j,i, count)
#                 if count==len(a)-(i+1):
#                     answer.append(-1)
#                     break
#
#         if a[i] == a[-1]:
#             answer.append(-1)
#     print(answer)
#     return answer
#
# re=list(map(int, input().split()))
# solution(re)
#
# def solution(s):
#     s.sort()
#     print(s)
#     max=s[-1]
#     min=s[0]
#     answer = '{} {}'.format(min, max)
#     return answer
#
# a=list(input().split())
# print(solution(a))

# def solution(s):
#     for i in range(len(s)):
#         if not s[i][0].isdecimal():
#             s[i] = s[i][0].upper() + s[i][1:].lower()
#     answer = ' '.join(s)
#     return answer
#
# a=input().split()
# print(solution(a))
#
# plus = [0 for i in range(len(A))]
# print(plus)

# n=int(input())
# arr = [1, 1]
#
# for i in range(n):
#     arr.append(arr[i] + arr[i + 1])
#
# print(arr[n - 1]%1234567)

from collections import deque

a=list(input())
for i in a:
    i
