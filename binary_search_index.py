def binary_search_index(data, key):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == key:
            return mid
        elif data [mid] < key :
            low = mid + 1
        else :
            high = mid - 1
            