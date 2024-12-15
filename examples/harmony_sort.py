################ HELPER METHODS ###############

def partition_harmoniously(arr, num_partitions):
    partitions = []
    part_size = int(len(arr) // num_partitions)   # Heuristically split into |k| quasi-equal parts

    for i in range(0, len(arr), part_size):
        partitions.append(arr[i:i + part_size])

    return partitions


def optimized_merge(part1, part2):
    """
    Merge 2 sorted arrays while keeping "order"
    """
    merged = []
    i = j = 0

    while i < len(part1) and j < len(part2):
        if part1[i] < part2[j]:
            merged.append(part1[i])
            i += 1
        else:
            merged.append(part2[j])
            j += 1

        # merge any remaining items from each part
        merged.extend(part1[i:])
        merged.extend(part2[j:])

    return merged

###############################################

def harmony_sort(arr, threshold, num_partitions):
    """ If the array size is smaller than the threshold the sort as O(n) 
    -   because harmony_sort time complexity is better when working on big arrays O(n log k) where k is the number of partitions
        which since is parallelized then is always <= n, thus executing in better time than comparison-based sorting algorithms which
        by default tend to run at best at O(n log n)
    """
    if len(arr) <= threshold:
        return sorted(arr)
    harmonic_partitions = partition_harmoniously(arr, num_partitions)
    # Parallelize the partitions sorting
    sorted_harmonic = [sorted(partition) for partition in harmonic_partitions]
    # Merged the sorted partitions harmoniously
    while len(sorted_harmonic) > 1:
        part1 = sorted_harmonic.pop(0)
        part2 = sorted_harmonic.pop(0)
        sorted_harmonic.append(optimized_merge(part1, part2))
    return sorted_harmonic[0]