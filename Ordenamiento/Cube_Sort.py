def cube_sort(arr, cube_size=5):
    if not arr:
        return arr
    
    # Asumimos datos 3D con estructura (x, y, z)
    min_x = min(p[0] for p in arr)
    min_y = min(p[1] for p in arr)
    min_z = min(p[2] for p in arr)
    max_x = max(p[0] for p in arr)
    max_y = max(p[1] for p in arr)
    max_z = max(p[2] for p in arr)
    
    x_buckets = int((max_x - min_x) / cube_size) + 1
    y_buckets = int((max_y - min_y) / cube_size) + 1
    z_buckets = int((max_z - min_z) / cube_size) + 1
    
    cubes = [[[ [] for _ in range(z_buckets)] 
             for _ in range(y_buckets)] 
             for _ in range(x_buckets)]
    
    for point in arr:
        x_idx = int((point[0] - min_x) / cube_size)
        y_idx = int((point[1] - min_y) / cube_size)
        z_idx = int((point[2] - min_z) / cube_size)
        cubes[x_idx][y_idx][z_idx].append(point)
    
    sorted_arr = []
    for x in range(x_buckets):
        for y in range(y_buckets):
            for z in range(z_buckets):
                # Ordenar cada cubo (podría usarse cualquier algoritmo)
                cubes[x][y][z].sort()
                sorted_arr.extend(cubes[x][y][z])
    
    return sorted_arr