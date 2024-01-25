def binary_search(array, value):
    low = 0
    high = len(array) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
            upper_bound = array[mid] if upper_bound is None or array[mid] < upper_bound else upper_bound
        else:
            return iterations, array[mid]

    return iterations, upper_bound


def main():
    array = [1.2, 2.5, 2.8, 3.7, 4.6, 4.7, 5.8, 6.9, 7.1, 7.3, 8.3, 9.6, 10.4]
    print(f"Homework 5 - Task 2 | Input array: {array}")
    element_to_find = array[8]
    print(f"Homework 5 - Task 2 | Find the result for the element {element_to_find}")
    result = binary_search(array, element_to_find)
    print(f"Homework 5 - Task 2 | The result is {result}")


if __name__ == "__main__":
    print(f"Homework 5 - Task 2 | Starting...\n")
    main()
    print(f"\nHomework 5 - Task 2 | Done")
