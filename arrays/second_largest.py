arr = [10, 5, 20, 8]

largest = arr[0]
second_largest = None

for x in arr[1:]:
    if x > largest:
        second_largest = largest
        largest = x
    elif x < largest and (second_largest is None or x > second_largest):
        second_largest = x

print(second_largest)
