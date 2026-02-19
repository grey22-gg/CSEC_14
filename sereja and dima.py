n = int(input())
c = list(map(int, input().split()))
left = 0
right = n - 1
s = 0
d = 0
t = 0
while left <= right:
    if c[left] > c[right]:
        choose = c[left]
        left += 1
    else:
        choose = c[right]
        right -= 1
    if t == 0:
        s += choose
    else:
        d += choose
    t = 1 - t
        
print(s,d)
