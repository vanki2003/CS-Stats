import random
def quicksort(array, left, right):
    if left < right:
        # Generate a random pivot index
        pivot_index = random_pivot(array, left, right)
        # Partition the array around the pivot and get the partition index
        partition_index = partition(array, left, right, pivot_index)
        # Recursively sort elements before and after partition
        quicksort(array, left, partition_index - 1)
        quicksort(array, partition_index + 1, right)

def random_pivot(array, left, right):
    return random.randint(left, right)

def partition(array, left, right, pivot_index):
    pivot_value = array[pivot_index]
    # Move pivot to the end
    swap(array, pivot_index, right)
    store_index = left
    
    # Compare remaining array elements against pivot
    for i in range(left, right):
        if array[i] < pivot_value:
            swap(array, i, store_index)
            store_index += 1
    # Move pivot to its final place
    swap(array, store_index, right)
    
    return store_index

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

# Example usage
array = [3, 6, 8, 10, 1, 2, 1]
quicksort(array, 0, len(array) - 1)
print(array)