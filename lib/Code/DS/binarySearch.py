def binarySearch(array, search_value):
    lower_bound = 0
    upper_bound = len(array) - 1

    try:
        while lower_bound <= upper_bound:

            mid_point = int((lower_bound + upper_bound) / 2)
            value_mid_point = array[mid_point]
            # print(value_mid_point)

            if search_value == value_mid_point:
                print("Value found at index position: ", array.index(value_mid_point))
                break
            elif search_value < value_mid_point:
                upper_bound = mid_point - 1
            elif search_value > value_mid_point:
                lower_bound = mid_point + 1
    except None:
        print("Not Found")


binarySearch([3, 17, 75, 80, 202], 800)
