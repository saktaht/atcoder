# def check_number(X):
#   checked_number = X**3 + X
#   if N == checked_number:
#     return X
#   elif N < checked_number:
#     return True
#   else:
#     return False

# N = int(input())

# # N = X**3 + X
# #   = X(x^2 + 1)
# #   = X(X + 1)(X + 1) - 2*X
  
# left = 0
# right = 10**5
# while left < right:
#   mid = (left + right) // 2
#   # print("mid:", mid)
#   answer = check_number(mid)
  
#   if answer == False:
#     left = mid 
#   if answer == True:
#     right = mid
#   if type(answer) == int:
#     left = answer
#     break

# print(left)

def check(x):
  return x**3 + x

N = int(input())
left = 0.0
right = 100.0

for i in range(100):
  mid = (left + right) / 2
  answer = check(mid)

  if answer < N:
    left = mid
  else:
    right = mid
print(mid)