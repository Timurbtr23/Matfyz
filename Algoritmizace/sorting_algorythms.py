def select_sort(a):
    """
    The selection sort is used when
        1. a small list is to be sorted
        2. cost of swapping does not matter
        3. checking of all the elements is compulsory
        4. cost of writing to a memory matters like in flash memory
            (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)
    """
    for step in range(len(a)):
        min_idx = step

        for i in range(step + 1, len(a)):
            # to sort in descending order, change > to < in this line
            if a[i] < a[min_idx]:
                min_idx = i

        a[step], a[min_idx] = a[min_idx], a[step]
    return a


def insert_sort(a):
    """
    The insertion sort is used when:
        1. the array is has a small number of elements
        2. there are only a few elements left to be sorted
    """
    for step in range(1, len(a)):
        key = a[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        a[j + 1] = key
    return a


def bubble_sort(a):
    """
    Bubble sort is used if
        1. complexity does not matter
        2. short and simple code is preferred
    """
    change = len(a)-1
    while change > 0:
        steps = change
        change = 0
        for j in range(steps):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                change = j
    return a


def merge_sort(array):
    """
    Merge Sort Applications
        Inversion count problem
        External sorting
        E-commerce applications
    n*log n
    """
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return array


def quick_sort(array, low, high):
    """
    Quicksort algorithm is used when
        the programming language is good for recursion
        time complexity matters
        space complexity matters
    quickSort(data, 0, size - 1)
    """
    # function to find the partition position
    def partition(array, low, high):

        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # return the position from where partition is done
        return i + 1

    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


def counting_sort(array):
    """
    Counting sort is used when:
        there are smaller integers with multiple counts.
        linear complexity is the need.
    O(n+k)
    """
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * (max(array)+1)

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, max(array)+1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

    return array


# Main function to implement radix sort
def radix_sort(array):
    """
    Radix sort is implemented in
        DC3 algorithm (Kärkkäinen-Sanders-Burkhardt) while making a suffix array.
        places where there are numbers in large ranges.
    data = [121, 432, 564, 23, 1, 45, 788]
    """

    def countingSort(array, place):
        size = len(array)
        output = [0] * size
        count = [0] * (max(array)+1)

        # Calculate count of elements
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, max(array)+1):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]

    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


def bucket_sort(array):
    """
    Bucket sort is used when:
        input is uniformly distributed over a range.
        there are floating point values
    """
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


def shell_sort(array, n):
    """
    Shell sort is used when:
        Insertion sort does not perform well when the close elements are far apart. Shell sort helps in reducing
         the distance between the close elements. Thus, there will be less number of swappings to be performed.
    average O(nlog n)
    """
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


# data = [4, 2, 2, 2, 2, 8, 3, 3, 1, 12]
