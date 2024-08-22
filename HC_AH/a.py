def remove_elements(list1, list2):
    print("Original lists:")
    print("List 1:", list1)
    print("List 2:", list2)

    # Method 1: List Comprehension
    result_comprehension = [item for item in list1 if item not in list2]
    print("\nMethod 1 (List Comprehension):")
    print(result_comprehension)

    # Method 2: Set Difference
    result_set = list(set(list1) - set(list2))
    print("\nMethod 2 (Set Difference):")
    print(result_set)

    # Method 3: Filter() function
    result_filter = list(filter(lambda x: x not in list2, list1))
    print("\nMethod 3 (Filter function):")
    print(result_filter)

# Example usage
list1 = [1,1 ,2 ,3, 4, 5, 5, 7, 6, 9, 10]
list2 = [11 ,12 ,13, 4, 5, 6, 7 ,18 ,19 ,20]

remove_elements(list1, list2)