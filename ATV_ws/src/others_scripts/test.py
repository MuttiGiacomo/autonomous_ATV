from collections import deque


a = deque([])
a.append("12")
a.append("24")
print(a.popleft())
print(bool(a))
print(a.popleft())
print(bool(a))

