def InsertionSort_1(array):
    for i in range(1, len(array)):
        temp_value = array[i]
        j = i - 1
        while j >= 0 and temp_value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp_value
