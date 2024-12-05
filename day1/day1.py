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

#---------Part 2-----------------

#reusing sorted lists from above 
#col0 = quick_sort(arr0)
#col1 = quick_sort(arr1)

def count_values(array, key):
    count_dict = {}  # Array to keep count
    for k in key:    
        for value in array:
            if value == k:
                # If the key is already in the dictionary, increment its count
                if k in count_dict:
                    count_dict[k] += 1
                else:
                    # Add the key with an initial count of 1
                    count_dict[k] = 1
            else:
                # If the key doesn't appear in the array col1, assign 0
                count_dict.get(k, 0)
        
    
    return count_dict

 
def sim_score(count_dict):  #to get similarity score
    sum = 0
    for key, value in count_dict.items():
        sum = sum + (key * value)
    return print(sum)



count = count_values(col1, col0)
sim_score(count)

#Answer:    = 26859182 
