from collections import deque
stack = deque()

stack.append('first')
stack.append('second')
stack.append('third')

print(stack)

print(stack.pop())  # Output: 'third'
print(stack.pop())  # Output: 'second'
print(stack.pop())  # Output: 'first'

stack.appendleft('zero')
stack.appendleft('one')
stack.appendleft('two')
stack.appendleft('three')
stack.appendleft('four')
print(stack)

print(stack.popleft())  # Output: 'four'
print(stack.popleft())  # Output: 'three'
print(stack.popleft())  # Output: 'two'
print(stack.popleft())  # Output: 'one'
print(stack.popleft())  # Output: 'zero'

print(stack)
