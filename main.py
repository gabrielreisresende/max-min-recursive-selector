def select_max_and_min(array, min_value, max_value):
    if len(array) == 1:
        min_value = min(min_value, array[0])
        max_value = max(max_value, array[0])
        return min_value, max_value
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    min_value, max_value = select_max_and_min(left, min_value, max_value)
    min_value, max_value = select_max_and_min(right, min_value, max_value)
    
    return min_value, max_value

array = [3, 4, 1, 2]
min_value, max_value = select_max_and_min(array, float('inf'), float('-inf'))
print(f"Maior elemento: {max_value}")
print(f"Menor elemento: {min_value}")
