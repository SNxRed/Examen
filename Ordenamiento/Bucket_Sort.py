def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)
    
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        buckets[int((num - min_val) // bucket_size)].append(num)
    
    arr = []
    for bucket in buckets:
        insertion_sort(bucket)  # Puede usarse otro algoritmo
        arr.extend(bucket)
    
    return arr