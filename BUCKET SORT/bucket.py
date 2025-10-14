def bucket_sort(arr):
  
    buckets = [[] for _ in range(len(arr))]
    
    
    for num in arr:
        index = int(num * len(arr))  
        buckets[index].append(num)
    
   
    for bucket in buckets:
        bucket.sort()
   
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array


datos = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47]
print(bucket_sort(datos))
