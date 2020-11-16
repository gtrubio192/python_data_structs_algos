def merge_sorted(arr1,arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        # 1. Compate first element in each list and append smaller element
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            # Step 3
            i += 1
        else:
            sorted_arr.append(arr2[j])
            # Step 3
            j += 1
        print(sorted_arr)

    # Since there might be remaining elems, loop through and add them to list
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[i])
        i += 1

    #print(f"Left list index i is {i} and has value: {arr1[i]}")
    #print(f"Right list index j is {j} and has value: {arr2[j]}")
    return sorted_arr

# xxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx
l1 = [6,1,4,11,6,8,10, 7]
l2 = [2,3,5,7,8,9]
print(f"Merged list: {merge_sorted(l1,l2)}")


# Steps
# 1. Compate first element in each list and append smaller element
# 2. Using indeces and an iterator perform same comparision
#    for all elements in both lists
# 3. Move marker up by 1 position after smaller number is found
# 4. Copy remaining list once comparisions are complete and there
#    are items still remaining in one of the lists
