import random
import time
import heapq
#1
with open('pantadeusz.txt', encoding='UTF-8') as f:
    print(str(f.read()))

#2
with open('pantadeusz.txt', 'r', encoding='UTF-8') as f:
    text = f.read()
    row = text.split('\n')
    for index, value in enumerate(row):
        print(f'{index}: {value}')
    print(row[8])

#3
random_numbers = [random.randint(0, 9999) for _ in range(50)]

for number in random_numbers:
    print(number)

'''
#4

def heap_sort(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)

    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))

    return sorted_arr


numbers = [4, 10, 11, 5, 73, 5, 1]
sorted_numbers = heap_sort(numbers)
print(sorted_numbers)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(greater)

numbers = [4, 10, 11, 5, 73, 5, 1]

start_time = time.time()
heap_sorted = heap_sort(numbers)
heap_sort_time = time.time() - start_time

start_time = time.time()
quick_sorted = quick_sort(numbers)
quick_sort_time = time.time() - start_time

print("Sortowanie kopcowe:")
print(heap_sorted)
print("Czas wykonania: %.6f sekund" % heap_sort_time)

print("\nSortowanie szybkie:")
print(quick_sorted)
print("Czas wykonania: %.6f sekund" % quick_sort_time)

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

filename = 'input.txt'
numbers = read_numbers_from_file(filename)
sorted_numbers = heap_sort(numbers)
print(sorted_numbers)