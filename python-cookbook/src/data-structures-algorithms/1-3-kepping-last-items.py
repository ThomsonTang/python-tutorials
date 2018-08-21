"""1.3 Keeping the last N items

The following code performs a simple text match on a sequence of lines and yields the matching line along with the
previous N lines of context when found.

When writing code to search for items, it is common to use a generator function involving yield, as shown in this 
recipe's solution.
"""

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# example use on a file
if __name__ == '__main__':
    with open('1-3-test-file.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

# using dequeue(maxlen=N) creates a fixed-sized queue.
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)

print(q)

"""
More generally, a deque can be used whenever you need a simple queue structure. If you don't give it a maximum size, you
get an unbounded queue that lets you append and pop items on either end.

Adding or popping items from either end of a queue has O(1) complexity. This is unlike a list where inserting or 
removing items from the front of the list is O(N).
"""
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)

q.appendleft(4)
print(q)

print(q.pop())
print(q)
print(q.popleft())
print(q)
