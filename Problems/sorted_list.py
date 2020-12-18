from sortedcontainers import SortedList

# Implementation of SortedList
# It keeps the sorted structure
# Insertion O(N) -> .add((val, "key"))
# Access O(1)

sorted_data = SortedList()

# Add multiple key,value pair
sorted_data.update([(100, "MSFT"), (400, "APPL"), (200, "GOOGL")])

# Add one key,value pair
sorted_data.add((300, "AMZN"))

print(sorted_data)


# Print the first N stock
def first_n_traded_stock(sorted_list, n):
    print(sorted_list[-n:])


first_n_traded_stock(sorted_data, 3)

# There is also a heapq implementation which is O(nlogn)
# https://stackoverflow.com/a/38833175/9209546

import heapq
from operator import itemgetter

heap_lst = [(100, 'Smallest'), (1000, 'Smaller'), (500, 'Small'), (3000, 'Big'),
            (4000, 'Bigger'), (5000, 'Biggest')]

key_value = {k: v for k, v in heap_lst}

heap = heapq.nlargest(3, key_value.items(), key=itemgetter(0))  # <- This!
print(heap)

# Re-map to get only the keys.
# res = list(map(itemgetter(0), heap))
# print(res)


# PS. Only if I knew these during Bloomberg interview. :D
