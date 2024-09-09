from datetime import datetime
import random



def radix_sort_with_buckets(arr):
    count = 0;
    if not arr:
        return arr
    
    max_num = max(arr)
    pos = 1
    while max_num // pos > 0:
        buckets = [[] for _ in range(10)]
        count +=1
        for number in arr:
            digit = (number // pos) % 10
            buckets[digit].append(number)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        
        pos *= 10
    
    print("Count, ", count)
    return arr


def radix_sort_with_counting(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = (arr[i] // exp) % 10

n = 10000
min_value = 0
max_value = 10000
l = [random.randint(min_value, max_value) for _ in range(n)]

print("Sorted list:")
starttime1 = datetime.now()

print()
print("BUCKET SORT")
print(radix_sort_with_buckets(l))
endtime1 = datetime.now()
print("\nTime taken:")
print((endtime1.timestamp() * 1000 - starttime1.timestamp() * 1000), " ms")
