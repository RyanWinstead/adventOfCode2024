import numpy as np

# Load the data
data = np.loadtxt("day1/input.txt")



#algorithm from chatgpt
def quick_sort(arr):
    if len(arr) <= 1:  # Base case: arrays with 0 or 1 element are already sorted
        return arr
    else:
        pivot = arr[0]  # Choose the first element as the pivot
        # Partition the array into elements less than, equal to, and greater than the pivot
        # Use NumPy's Boolean indexing to filter the array
        less = arr[1:][arr[1:] <= pivot]
        greater = arr[1:][arr[1:] > pivot]
        return np.concatenate((quick_sort(less), [pivot], quick_sort(greater)))
    
#split columns into their own numpy arrays
arr0 = data[:, 0]
arr1 = data[:, 1]

#sort those new arrays
col0 = quick_sort(arr0)
col1 = quick_sort(arr1)

#get distances and sum
grand=0
for x,y in zip(col0, col1):
    grand = grand + abs(x-y)
print(grand)



#Answer:   = 1320851 

