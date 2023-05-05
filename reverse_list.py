"""
Give a list l, swap the items at index i and index j
"""
def swap_items_inplace(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


"""
Reverse the items in a list using swap_items_inplace()
"""
def reverse_list_inplace(l):
    length = len(l)
    for i in range(length//2):
        j = length - i - 1
        swap_items_inplace(l, i, j)
        



"""
Little testing function that compares if actual result is the same as expected result
"""
def test_reverse_list(case_num, actual, expected):
    print("Test " + str(case_num) + ": ", end="")
    if actual == expected:
        print("Passed")
    else:
        print("Failed")



if __name__ == "__main__":
    # Test case 1
    test1 = [1]
    reverse_list_inplace(test1)
    test_reverse_list(1, test1, [1])

    # Test case 2
    test2 = [1, 2]
    reverse_list_inplace(test2)
    test_reverse_list(2, test2, [2,1])

    # Test case 3
    test3 = [1,2,3]
    reverse_list_inplace(test3)
    test_reverse_list(3, test3, [3,2,1])
    

    # Test case 4
    test4 = [1,2,3,4]
    reverse_list_inplace(test4)
    test_reverse_list(4, test4, [4,3,2,1])


    # Test case 5
    test5 = [1,2,3,4,5]
    reverse_list_inplace(test5)
    test_reverse_list(5, test5, [5,4,3,2,1])
    

    # Test case 6
    test6 = [1,2,3,4,5,6]
    reverse_list_inplace(test6)
    test_reverse_list(6, test6, [6,5,4,3,2,1])

    
