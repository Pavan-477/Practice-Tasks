from collections import deque
stack=deque()
n=input('enter a number : ')
for i in n:
    stack.append(i)

for j in range(len(stack)):
    print(stack.pop(),end='')