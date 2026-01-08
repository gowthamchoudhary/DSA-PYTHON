#given an array of integers print the elements find max min and sum of the elements\
# Time Complexity: O(n)
# Space Complexity: O(1)
def basic_array_operations(arr):
    max = arr[0]
    min = arr[0]    
    sum = 0
    for i in arr:
        print(i)
        if i > max:
            max = i
        if i < min:
            min = i
        sum += i
    print("Max:", max)
    print("Min:", min)
    print("Sum:", sum)

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 7]
    basic_array_operations(arr)
