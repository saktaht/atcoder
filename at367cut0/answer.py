X = float(input())
s = '{:f}'.format(X).rstrip('0').rstrip('.')
print(s)