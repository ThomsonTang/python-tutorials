"""1.4 Finding the Largest or Smallest N Items

The heapq module has two functions--nlargest() and nsmallest()--that do this exactly.
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# Both functions also accept a key parameter that allows them to be used with more complicated data structure.
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'APPLE', 'shares': 50, 'price': 543.22},
    {'name': 'FACEBOOK', 'shares': 200, 'price': 21.09}
]

cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['shares'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['shares'])
print(cheap)
print(expensive)

heap = list(nums)
heapq.heapify(heap)
print(heap)
