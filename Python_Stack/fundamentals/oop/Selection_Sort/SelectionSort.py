def SelectionSort(array):
    length_array = len(array)
    for i in range(length_array):
        current_value = array[i]
        current_index = i
        minimum_value = current_value
        minimum_index = None
        j = i + 1
        while j < length_array:
            if array[j] < minimum_value:
                minimum_value = array[j]
                minimum_index = j
            j += 1
        if minimum_index:
            array[current_index], array[minimum_index] = array[minimum_index], array[current_index]

    return array



