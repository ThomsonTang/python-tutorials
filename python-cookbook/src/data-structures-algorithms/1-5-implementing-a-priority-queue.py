"""1.5 Implementing a Priority Queue

Priority Queue: a queue that sorts items by a given priority and always returns the item with the highest priority on
each pop operation.

The following class uses the `heapq` module to implement a simple priority queue.
"""

import heapq


class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# An Example of How It be Used.
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('Thomson'), 1)
q.push(Item('Lisa'), 4)
q.push(Item('Timmy'), 5)
q.push(Item('Others'), 1)
q.pop()

""" Discussion
## The Core Points
the core of this recipe concerns the use of the `heapq` module.

1. `heapq.heappush()` and `heapq.heappop()` functions: insert and remove items from a list `_queue` in a way such that 
the first item in the list has the smallest priority.
2. Correctness: The `heappop()` method always returns the "smallest" item, so that is the key to making the queue pop 
the correct items.
3. Fairness: Since the push and pop operation have `O(logN)` complexity where N is the number of items in the heap, they
are fairly efficient even for fairly large values of N.


## The Important Tuples 
In this recipe, the queue consists of tuples of the form `(-priority, index, item)`.

1. The `priority` value is negated to get the queue to sort items from highest priority to lowest priority. This is 
opposite of the normal heap ordering.
2. The `index` value is to properly order items with the same priority level and serves an important role in making the 
comparison operations work for items that have the same priority level.
"""
