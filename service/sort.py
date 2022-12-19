def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# function to perform quicksort


def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


def gnomeSort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr

# def gnome_sort(arr, i):
#     if i >= len(arr):
#         return arr
#     if arr[i-1] > arr[i]:
#         arr[i], arr[i-1] = arr[i-1], arr[i]
#         return gnome_sort(arr, i-1)
#     return gnome_sort(arr, i+1)
#
# def sort(a, pos=0):
#     if pos < len(a):
#         if pos == 0 or a[pos] >= a[pos - 1]:
#             sort(a, pos + 1)
#         else:
#             a[pos], a[pos - 1] = a[pos - 1], a[pos]
#             sort(a, pos - 1)