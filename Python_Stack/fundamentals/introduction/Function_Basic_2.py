def countdown(number):
    return [i for i in range(number, -1, -1)]


print(countdown(5))


def print_and_return(arr):
    print(arr[0])
    return arr[-1]


print(print_and_return([1, 2]))


def first_plus_length(arr):
    return arr[0] + len(arr)


print(first_plus_length([1, 2, 3, 4, 5]))


def values_greater_than_second(arr):
    if len(arr) < 2:
        return False

    value = arr[1]
    temp = []
    for item in arr:
        if item > value:
            temp.append(item)
    return temp


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))


def length_and_value(length, value):
    return [value] * length


print(length_and_value(4, 7))
print(length_and_value(6, 2))
