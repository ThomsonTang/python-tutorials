"""
# 1.6 Mapping Keys to Multiple Values in a Dictionary

## Solution

If you want to map keys to multiple values, you need to store the multiple values in another container such as list or
set. For example:

```python
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}
```

```java
Map<String, List<Integer>> map = Maps.newHashMap();
map.put("a", Lists.of(1, 2, 3));
map.put("b", Lists.of(4, 5));

Map<String, Set<Integer>> map = Maps.newHashMap();
...
...
```

### How to choice list or set

> Use a list if you want to preserve the insertion order of the items.
> Use a set if you want to eliminate duplicates (and don't care about the order).

### `defaultdict`

To easily construct such dictionaries, you can use `defaultdict` in the `collections` module.

"""

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
